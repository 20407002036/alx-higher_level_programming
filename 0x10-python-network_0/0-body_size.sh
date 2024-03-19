#!/bin/bash
# body size of the reposnse
if [ -z "$1" ]; then echo "Usage: $0 <URL>"; exit 1; fi

response=$(curl -sI "$1"); size=$(echo -n "$response" | grep -iE '^Content-Length:' | awk '{print $2}' | tr -d '\r'); echo "$size"
