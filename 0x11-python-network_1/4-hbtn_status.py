#!/usr/bin/python3
""" Script that fetches https://intranet.hbtn.io/status  """

import urllib.request

if __name__ == '__main__':
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as req:
        page = req.read()
        print("Body response:")
        print("\t- type: {}".format(type(page)))
        print("\t- Body response: {}".format(page.decode("utf-8")))
