# library: bs4

# import urllib3
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Dublin"

try:

    page = urlopen(url)
except Exception as e:
    print(f"error occured: {e}")


try:

    soup = BeautifulSoup(page, 'html.parser')
    print(soup)
    print(soup.prettify())
except Exception as e:
    print(e)

