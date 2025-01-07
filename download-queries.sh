#!/bin/bash

set -e

OWNER=team-plain
REPO=typescript-sdk
BRANCH=main
FOLDERS=("fragments" "mutations" "queries")

download_files() {
    local folder=$1
    local api_url="https://api.github.com/repos/$OWNER/$REPO/contents/src/graphql/$folder?ref=$BRANCH"

    # Get list of files in the folder
    local files=$(curl -s "$api_url" | jq -r '.[].download_url')

    if [ -z "$files" ]; then
        echo "Error: No files found or invalid repository/folder: $folder"
        exit 1
    fi

    # Download each file
    for file in $files; do
        local filename=$(basename "$file")
        echo "Downloading $filename from $folder..."
        mkdir -p "graphql/$folder"
        curl -s -L "$file" -o "graphql/$folder/$filename"
    done
}

rm -rf graphql
for folder in "${FOLDERS[@]}"; do
    mkdir -p "graphql/$folder"
    download_files "$folder"
done
