#!/usr/bin/env bash
set -euo pipefail

checkout=$(mktemp -d)
trap 'rm -rf "$checkout"' EXIT

curl --fail --location --silent --show-error \
    https://raw.githubusercontent.com/team-plain/sdk/main/packages/graphql/src/_generated_documents.graphql \
    -o "$checkout/documents.graphql"
test -s "$checkout/documents.graphql"

rm -rf graphql
mkdir graphql
cp "$checkout/documents.graphql" graphql/
