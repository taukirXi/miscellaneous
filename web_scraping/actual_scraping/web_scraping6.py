"""
parsing a web page using bsr 
url = https://docs.python.org/3/
"""

import requests
from bs4 import BeautifulSoup
url = "https://docs.python.org/3/"

response = requests.get(url)
# if there xml data then user lxml parser
soup = BeautifulSoup(response.content, 'html.parser')
print(soup.prettify())
