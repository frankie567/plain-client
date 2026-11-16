# Changelog

All notable changes to this project will be documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Changed

- Lazily import generated client models and defer Pydantic model building until first use to reduce startup time and memory.
- Fetch the schema and GraphQL documents from Plain's new `team-plain/sdk` repository and regenerate the client.
- Expand the generated client from 71 to 623 operations. Breaking: upstream replaces `customer_by_id`, `customer_group_by_id`, and `user_by_id` with `customer`, `customer_group`, and `user`, and removes `customer_customer_groups`, `customer_tenants`, and `index_document`. Generated response models and operation names also change.
- Require Python 3.11 or newer; test Python 3.11–3.15.
- Use HTTPX2 for HTTP requests. Custom clients must now be `httpx2.AsyncClient` instances.
- Upgrade dependencies and adopt uv, just, Ruff, ty, pre-commit, and Zensical.
- Publish tested release artifacts using signed tags, PyPI trusted publishing, and build attestations.
