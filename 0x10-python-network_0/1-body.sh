#!/bin/bash
# Script that takes in a URL, sends a GET request to the URL
curl -X GET -L "$1"
