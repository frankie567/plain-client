#!/usr/bin/env bash
set -euo pipefail

checkout=$(mktemp -d)
trap 'rm -rf "$checkout"' EXIT

git clone --depth 1 https://github.com/team-plain/typescript-sdk.git "$checkout/sdk"
for folder in fragments mutations queries; do
    test -n "$(find "$checkout/sdk/src/graphql/$folder" -name '*.gql' -print -quit)"
done

rm -rf graphql
mkdir graphql
for folder in fragments mutations queries; do
    cp -R "$checkout/sdk/src/graphql/$folder" graphql/
done
