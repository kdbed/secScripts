#!/usr/bin/python3
import requests
import os

while True:
    file = input("file: ")
    url = f"http://icinga.cerberus.local:8080/icingaweb2/lib/icinga/icinga-phpthirdparty{file}"
    r = requests.get(url)
    print(r.text)


####
