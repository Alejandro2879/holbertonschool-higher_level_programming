#!/usr/bin/python3
""" cript that takes in a URL and an email, sends a POST request  """
import sys
import urllib.request
if __name__ == '__main__':
    url = sys.argv[1]
    value = sys.argv[2]
    email = {'email': value}
    data = urllib.parse.urlencode(email)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        page = response.read()
        print(page.decode("utf-8"))
