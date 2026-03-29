#!/bin/bash
# displays size of response body
curl -s "$1" | wc -c
