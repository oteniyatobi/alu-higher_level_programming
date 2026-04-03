#!/usr/bin/python3
"""Takes a URL and displays the value of X-Request-Id in the response header."""
import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as r:
        print(r.headers.get('X-Request-Id'))
