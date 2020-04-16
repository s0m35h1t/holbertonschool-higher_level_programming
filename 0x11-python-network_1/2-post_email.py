#!/usr/bin/python3
"""
takes in a URL and an email, sends a POST request to the passed URL with the
email as a parameter, and displays the body of the response
"""
import urllib.parse as parse
import urllib.request as request
from sys import argv

if __name__ == "__main__":
    data = parse.urlencode({'email': argv[2]}).encode('utf-8')
    req = request.Request(argv[1], data)
    with request.urlopen(req) as r:
        print(r.read().decode('utf-8'))
