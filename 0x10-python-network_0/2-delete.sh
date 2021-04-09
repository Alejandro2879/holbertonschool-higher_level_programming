#!/bin/bash
#Script that sends a DELETE request to the URL passed as the first argument
curl -s DELETE "$1"
