# David Ziama
# Class ID 3
# Write a simple program that parse a wikipage then extract the headers of the page.

import requests
from bs4 import BeautifulSoup
import os


#created by saria goudarzvand
#edited by David

url = "https://en.wikipedia.org/wiki/Rick_and_Morty"
source_code = requests.get(url)
plain_text = source_code.text
soup = BeautifulSoup(plain_text, "html.parser")
result_list = soup.findAll('div')
for div in result_list:
        r1 = div.find('h1')
        print(r1)
for div in result_list:
        r2 = div.find('h2')
        print(r2)


url = "https://en.wikipedia.org/wiki/Rick_and_Morty"
source_code = requests.get(url)
plain_text = source_code.text
soup = BeautifulSoup(plain_text, "html.parser")
result_list = soup.findAll('body')
for div in result_list:
        r1 = div.find('h1')
        print(r1)