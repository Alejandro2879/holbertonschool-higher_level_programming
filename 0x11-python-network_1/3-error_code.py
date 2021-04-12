#!/usr/bin/python3
"""
cript that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).
"""

import sys
import urllib.request


if __name__ == '__main__':
    url = sys.atgv[1]
    try:
        with urllib.request.urlopen(url) as req:
        my_req = req.read()
        print(page.decode("utf-8"))
    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.code))
