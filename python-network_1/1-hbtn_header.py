#!/usr/bin/python3
"""Sends a request and displays the X-Request-Id response header value."""
import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as r:
        print(r.headers.get('X-Request-Id'))
