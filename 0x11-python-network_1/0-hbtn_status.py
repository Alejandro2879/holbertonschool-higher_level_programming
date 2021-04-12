#!/usr/bin/python3
""" Script that fetches https://intranet.hbtn.io/status """
import urllib.request


with urllib.request.urlopen('https://intranet.hbtn.io/status') as resp:
    print(resp.read())
