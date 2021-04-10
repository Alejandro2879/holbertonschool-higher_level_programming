#!/bin/bash                                                                                                                
# Script that takes in a URL and displays all HTTP methods the server will accept.                                         
curl -s -I "$1" | grep "Allow" | cut --complement -b 1-7 --complement
