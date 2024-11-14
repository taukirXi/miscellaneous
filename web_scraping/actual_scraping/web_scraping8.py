"""
parsing a web page using bsr 

"""

import requests
from bs4 import BeautifulSoup


url = "https://books.toscrape.com/index.html"

response = requests.get(url)

# if there xml data then user lxml parser
soup = BeautifulSoup(response.content, 'html.parser')


# print(soup.prettify())

articles = soup.find_all('article')

# print(articles)

# input("for product pod in article: ")
for article in articles:
    product_pods = article.find_all(class_='product_price')

    # for product_pod in product_pods:
    #     print(f"{product_pod}\n\n")
    # print(product_pods)
    for product in product_pods:
        price = product.find('p', class_='price_color').text.strip()
        print(price)
