# https://just.systems

install:
    uv sync --locked --all-extras
    uv run --locked pre-commit install

lint:
    uv run --locked ruff check --fix .
    uv run --locked ruff format .
    uv run --locked --all-extras ty check plain_client/ tests/

lint-check:
    uv run --locked ruff format --check .
    uv run --locked ruff check .
    uv run --locked --all-extras ty check plain_client/ tests/

test:
    uv run --locked --all-extras pytest

test-cov-xml:
    uv run --locked --all-extras pytest --cov-report=xml

docs-serve:
    uv run --locked zensical serve

docs-build:
    uv run --locked zensical build --strict

build:
    uv run --locked --all-extras uv build --no-build-isolation

version bump:
    #!/usr/bin/env bash
    set -euo pipefail
    if [ -n "$(git status --porcelain)" ]; then
        echo "Commit or stash changes before preparing a release." >&2
        exit 1
    fi
    uv sync --locked --all-extras
    if ! uv run --no-sync python -c '
    import keepachangelog

    unreleased = keepachangelog.to_dict("CHANGELOG.md", show_unreleased=True).get("unreleased", {})
    raise SystemExit(not any(entries for category, entries in unreleased.items() if category != "metadata"))
    '; then
        echo "Add release notes under Unreleased in CHANGELOG.md." >&2
        exit 1
    fi
    previous_version="$(uv run --no-sync hatchling version)"
    uv run --no-sync hatchling version {{quote(bump)}}
    release_version="$(uv run --no-sync hatchling version)"
    if [[ ! "$release_version" =~ ^[0-9]+\.[0-9]+\.[0-9]+([ab][0-9]+|rc[0-9]+)?$ ]]; then
        git restore -- plain_client/__version__.py
        echo "Use a final, alpha, beta, or release candidate version." >&2
        exit 1
    fi
    if [[ "$release_version" == "$previous_version" ]]; then
        echo "The version bump must change the version." >&2
        exit 1
    fi
    uv run --no-sync keepachangelog release "$release_version"
    test -n "$(uv run --no-sync keepachangelog show "$release_version")"
    uv lock
    git add plain_client/__version__.py CHANGELOG.md uv.lock
    git commit -S -e -m "release: Bump version to $release_version"

release pr:
    #!/usr/bin/env bash
    set -euo pipefail
    pr={{quote(pr)}}
    if [[ ! "$pr" =~ ^[1-9][0-9]*$ ]]; then
        echo "Provide a pull request number." >&2
        exit 1
    fi
    release_commit="$(gh pr view --repo frankie567/plain-client \
        --json state,baseRefName,mergeCommit,files \
        --jq 'select(.state == "MERGED" and .baseRefName == "main")
              | select(any(.files[]; .path == "plain_client/__version__.py")
                       and any(.files[]; .path == "CHANGELOG.md"))
              | .mergeCommit.oid // empty' -- "$pr")"
    if [[ -z "$release_commit" ]]; then
        echo "Provide a merged release PR targeting main that updates the version and changelog." >&2
        exit 1
    fi
    git fetch --no-tags origin refs/heads/main
    if ! git merge-base --is-ancestor "$release_commit" FETCH_HEAD; then
        echo "The release commit must be on origin/main." >&2
        exit 1
    fi
    release_version="$(git show "$release_commit:plain_client/__version__.py" | sed -n 's/^__version__ = "\([^"]*\)"$/\1/p')"
    if [[ ! "$release_version" =~ ^[0-9]+\.[0-9]+\.[0-9]+([ab][0-9]+|rc[0-9]+)?$ ]]; then
        echo "The release commit must contain a valid release version." >&2
        exit 1
    fi
    release_notes="$(git show "$release_commit:CHANGELOG.md" | uv run --locked keepachangelog show "$release_version" /dev/stdin)"
    test -n "$release_notes"
    tag="v$release_version"
    git tag -s "$tag" "$release_commit" -m "Release $release_version"
    git push --no-follow-tags origin "refs/tags/$tag"

release-notes version:
    @uv run --locked keepachangelog show {{quote(version)}}

download-schema:
    curl --fail --location --silent --show-error https://raw.githubusercontent.com/team-plain/sdk/main/packages/graphql/src/schema.graphql -o schema.graphql

download-queries:
    ./download-queries.sh

generate: download-schema download-queries generate-local

generate-local:
    uv run --locked ariadne-codegen
    just lint
