#!/bin/bash
# comment for how it works
if [ -z "$1" ]; then echo "Usage: $0 <URL>"; exit 1; fi
response=$(curl -s -o /dev/null -w "%{http_code}" "$1"); if [ "$response" -eq 200 ]; then curl -s "$1"; else echo "Response code is not 200 (OK)"; fi
