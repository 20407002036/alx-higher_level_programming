#!/bin/bash
# It takes a URL, sends a request to that URL, displays ize of the body of the response

if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send a GET request to the URL and store the response in a variable
response=$(curl -sI "$1")

# Extract the content-length header from the response and display the size in bytes

size=$(echo -n "$response" | wc -c)

echo "$content_length"
