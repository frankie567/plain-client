# Plain Client

<p align="center">
    <em>A Python client for Plain GraphQL API</em>
</p>

[![build](https://github.com/frankie567/plain-client/workflows/Build/badge.svg)](https://github.com/frankie567/plain-client/actions)
[![PyPI version](https://badge.fury.io/py/plain-client.svg)](https://badge.fury.io/py/plain-client)

---

**Documentation**: <a href="https://frankie567.github.io/plain-client/" target="_blank">https://frankie567.github.io/plain-client/</a>

**Source Code**: <a href="https://github.com/frankie567/plain-client" target="_blank">https://github.com/frankie567/plain-client</a>

---

> [!IMPORTANT]
> This client is generated **automatically** using:
> * [ariadne-codegen](https://github.com/mirumee/ariadne-codegen)
> * [Plain GraphQL Schema](https://core-api.uk.plain.com/graphql/v1/schema.graphql)
> * Fragments, mutations and queries provided by Plain in their [official TypeScript SDK](https://github.com/team-plain/typescript-sdk/tree/main/src/graphql)

## Quickstart

Requires Python 3.11 or newer. The client uses HTTPX2; pass an
`httpx2.AsyncClient` when supplying a custom HTTP client.

```bash
pip install plain-client
```

```py
from plain_client import Plain

client = Plain(
    "https://core-api.uk.plain.com/graphql/v1", {"Authorization": "Bearer YOUR_API_KEY"}
)


async def get_thread():
    return await client.thread("THREAD_ID")
```

## Development

### Setup environment

Install [uv](https://docs.astral.sh/uv/) and [just](https://just.systems/). Use Python 3.11 or newer.

Install the development dependencies and pre-commit hooks with `just install`.

### Generate the client

Run `just generate` to download the current Plain schema and the fragments,
mutations, and queries from Plain's TypeScript SDK and regenerate the client.
Use `just generate-local` to regenerate from the existing downloads.
Generation requires Git and curl.

### Run unit tests

```bash
just test
```

### Format the code

Run Ruff to format and lint the code, then check types with ty.

```bash
just lint
```

Use `just lint-check` to run the same checks without editing files.

### Publishing a release

1. Commit the release notes under `Unreleased` in [CHANGELOG.md](CHANGELOG.md).
   From a clean release branch with Git signing configured, run `just version patch`,
   `just version minor`, or `just version major`. The recipe updates the version,
   changelog, and lockfile, then opens your Git editor for the signed commit.
2. Preview the release notes with `just release-notes <version>`, then push the
   branch and merge the release PR into `main`.
3. With the GitHub CLI authenticated, run `just release <PR number>`. This signs
   and pushes a tag pointing to the merged PR commit. After the checks pass,
   CI publishes the distributions to PyPI with attestations and publishes the
   GitHub release with build provenance.

The PyPI Trusted Publisher must match the `build.yml` workflow and the GitHub
`release` environment.

## Serve the documentation

The documentation uses Zensical. Start the local preview with the following command.

```bash
just docs-serve
```

Open http://localhost:8000. The preview reloads when documentation changes.
Edit pages in `docs/` and configure the site in `zensical.toml`.

Build the static site into `site/` with the following command.

```bash
just docs-build
```


## License

This project is licensed under the terms of the MIT license.
