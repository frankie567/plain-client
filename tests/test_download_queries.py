import os
import subprocess
from pathlib import Path

import pytest


@pytest.mark.parametrize("valid_checkout", [True, False])
def test_download_queries(tmp_path: Path, valid_checkout: bool) -> None:
    script = Path(__file__).resolve().parents[1] / "download-queries.sh"
    graphql = tmp_path / "graphql"
    graphql.mkdir()
    (graphql / "old.gql").write_text("old")
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    git = bin_dir / "git"
    git.write_text(
        "#!/usr/bin/env bash\nset -euo pipefail\n"
        "for folder in fragments mutations queries; do\n"
        '  mkdir -p "$5/src/graphql/$folder"\n'
        + ('  touch "$5/src/graphql/$folder/new.gql"\n' if valid_checkout else "")
        + "done\n"
    )
    git.chmod(0o755)
    result = subprocess.run(
        ["bash", str(script)],
        cwd=tmp_path,
        env={**os.environ, "PATH": f"{bin_dir}:{os.environ['PATH']}"},
        capture_output=True,
        text=True,
    )
    if valid_checkout:
        assert result.returncode == 0, result.stderr
        assert not (graphql / "old.gql").exists()
        assert len(list(graphql.glob("*/new.gql"))) == 3
    else:
        assert result.returncode != 0
        assert (graphql / "old.gql").read_text() == "old"
