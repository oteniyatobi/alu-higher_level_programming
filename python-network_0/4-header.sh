#!/bin/bash
# sends GET request with custom header
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
