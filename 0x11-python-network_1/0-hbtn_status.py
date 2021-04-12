#!/usr/bin/python3
""" Script that fetches https://intranet.hbtn.io/status """
import urllib.request

if __name__ == '__main__':

    with urllib.request.urlopen('http://0.0.0.0:5050/status') as resp:
        response = resp.read()
        print("- Body response:")
        print("\t- type: {}".format(type(response)))
        print("\t- content: {}".format(response))
        print("\t- utf8 content: {}".format(response.decode("UTF-8")))
