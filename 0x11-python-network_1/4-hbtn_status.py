#!/usr/bin/python3
""" Script that fetches https://intranet.hbtn.io/status  """

import requests


if __name__ == '__main__':
    page = requests.get('https://intranet.hbtn.io/status')
    new = page.content
    new = new.decode("utf-8")
    print("Body response:")
    print("\t- type: {}".format(type(new)))
    print("\t- Body response: {}".format(new))
