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

```bash
pip install plain-client
```

```py
from plain_client import Plain

client = Plain("https://core-api.uk.plain.com/graphql/v1", {"Authorization": "Bearer YOUR_API_KEY"})

async def get_thread():
    return await client.thread("THREAD_ID")
```

## Development

### Setup environment

We use [Hatch](https://hatch.pypa.io/latest/install/) to manage the development environment and production build. Ensure it's installed on your system.

### Generate the client

You can trigger a generation of the client with:

```bash
hatch run generate
```

It'll automatically download latest schema, fragments, mutations and queries provided by Plain.

### Run unit tests

You can run all the tests with:

```bash
hatch run test:test
```

### Publish a new version

You can bump the version, create a commit and associated tag with one command:

```bash
hatch version patch
```

```bash
hatch version minor
```

```bash
hatch version major
```

Your default Git text editor will open so you can add information about the release.

When you push the tag on GitHub, the workflow will automatically publish it on PyPi and a GitHub release will be created as draft.

## Serve the documentation

You can serve the Mkdocs documentation with:

```bash
hatch run docs-serve
```

It'll automatically watch for changes in your code.

## License

This project is licensed under the terms of the MIT license.
