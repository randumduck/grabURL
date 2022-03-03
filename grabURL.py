#!/usr/bin/python3
import sys
from requests_html import HTMLSession

a = sys.argv[1]

session = HTMLSession()

r = session.get('https://'+a)
for i in r.html.absolute_links:
        print(i)
