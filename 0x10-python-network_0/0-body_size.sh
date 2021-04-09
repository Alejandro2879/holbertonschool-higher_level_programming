#!/bin/bash
# Bash script that displays the size of the body of the response
curl -s -w %{size_download}\\n "$1"
