# Changelog

All notable changes to this project will be documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Changed

- Require Python 3.11 or newer; test Python 3.11–3.15.
- Use HTTPX2 for HTTP requests. Custom clients must now be `httpx2.AsyncClient` instances.
- Refresh generated operations and models against Plain's current schema and TypeScript SDK (commit `bb56b7274dca19d0bb8d2e4b569de86519b908e1`). This includes the `send_chat` operation and updated input and response fields.
- Upgrade dependencies and adopt uv, just, Ruff, ty, pre-commit, and Zensical.
- Publish tested release artifacts using signed tags, PyPI trusted publishing, and build attestations.
