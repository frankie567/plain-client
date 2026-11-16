import os
import subprocess
from pathlib import Path

import pytest


@pytest.mark.parametrize("download", ["success", "empty", "failure"])
def test_download_queries(tmp_path: Path, download: str) -> None:
    script = Path(__file__).resolve().parents[1] / "download-queries.sh"
    graphql = tmp_path / "graphql"
    graphql.mkdir()
    (graphql / "old.gql").write_text("old")
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    curl = bin_dir / "curl"
    curl.write_text(
        "#!/usr/bin/env bash\nset -euo pipefail\n"
        'test "$5" = "https://raw.githubusercontent.com/team-plain/sdk/main/'
        'packages/graphql/src/_generated_documents.graphql"\n'
        + {
            "success": 'echo "query Example { __typename }" > "$7"\n',
            "empty": 'touch "$7"\n',
            "failure": "exit 22\n",
        }[download]
    )
    curl.chmod(0o755)
    result = subprocess.run(
        ["bash", str(script)],
        cwd=tmp_path,
        check=False,
        env={**os.environ, "PATH": f"{bin_dir}:{os.environ['PATH']}"},
        capture_output=True,
        text=True,
    )
    if download == "success":
        assert result.returncode == 0, result.stderr
        assert not (graphql / "old.gql").exists()
        assert (graphql / "documents.graphql").read_text() == (
            "query Example { __typename }\n"
        )
    else:
        assert result.returncode != 0
        assert (graphql / "old.gql").read_text() == "old"
