"""
parsing a web page using bsr 
url = https://docs.python.org/3/
"""

import requests
from bs4 import BeautifulSoup


def list_all_the_p_tag(soup):
    return soup.find_all('p')


def list_all_the_a_tag(soup):
    return soup.find_all('a')


def left_pan_data(soup):
    return soup.find_all("div", class_="sphinxsidebarwrapper")


url = "https://docs.python.org/3/"

response = requests.get(url)

# if there xml data then user lxml parser
soup = BeautifulSoup(response.content, 'html.parser')

# print(soup.prettify())

# input("finding all the 'p' tags. continue?....")

# p_tags = list_all_the_p_tag(soup)

# for tag in p_tags:
#     print(tag)


# input("collecting all the links: ")
# a_tags = list_all_the_a_tag(soup)

# for tag in a_tags:
#     print(tag)


# left_pan = left_pan_data(soup)
left_pan = soup.find_all("div", class_="sphinxsidebarwrapper")
print(left_pan)


input("list all the a tag. continue....")
a_tags = left_pan.find_all('a')
# for tag in a_tags:
#     print(tag)


# input("lisint al the text. continee?,...")
# for div in left_pan:
#     a_tags = div.find_all('a')
#     for tag in a_tags:
#         print(tag.text)

