#!/usr/bin/env python3

import os
import json

# run cgi_server.py
# make script executable chmod +x hello.py
# test on browser with localhost:8080/hello.py

# Question 1
# print environment variables as plain text
# print("Content-Type: text/plain")
# print()
# print(os.environ)

# Question 2
# print environment variables as JSON
# print("Content-Type: application/json")
# print()
# print(json.dumps(dict(os.environ), indent=2))

# to fill the query string
# localhost:8080/hello.py?thisisaquery
# environment variable QUERY_STRING will be filled with it

# extract the value in variable QUERY_STRING
# print query parameter data in html
# test http://localhost:8080/hello.py?this
# print("COntent-Type: text/html")
# print()
# print(f"<p>QUEY_STRING={os.environ['QUERY_STRING']}</p>")

# Question 3: 
# extract the user's browser (environment variable HTTP_USER_AGENT)
print("COntent-Type: text/html")
print()
print(f"<p>QUEY_STRING={os.environ['HTTP_USER_AGENT']}</p>")