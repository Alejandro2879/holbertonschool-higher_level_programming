#!/usr/bin/python3
"""
Script that takes in a URL and an email address, sends a POST request to the
passed URL with the email as a parameter, and finally displays the body.
"""

import sys
import requests


if __name__ == '__main__':
    email = {'email': sys.argv[2]}
    url = sys.argv[1]

    req = requests.post(url, data=email)
    print(req.content.decode("utf-8"))
