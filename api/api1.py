# iterative server
# and concurent server


# using the rest apis

# get() and post()
import requests
import urllib.parse


import os
import folium
from geopy.geocoders import Nominatim as nt
# print(response.status_code)
# print(response.content)


def post_method():

    url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url)

    print(response.status_code)
    print(response.content)
    input("contine...?")

    doc1 = {
        "userId": 101,
        "title": "Making a post request",
        "body": "demo for the api students"
    }

    response = requests.post(url, doc1)

    if (response.status_code > 199):
        print(response.json())


# post the data into below url
def todo_posts():
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)

    doc2 = {
        "userId": 101,
        "title": "Making a post request",
        "completed": True
    }

    response = requests.post(url, doc2)
    if (response.status_code > 199):
        print(response.json())


# updating the data using put mehtod


def using_put():
    url = "https://jsonplaceholder.typicode.com/todos/20"

    doc3 = {
        "userId": 101,
        "title": "Making a post request",
        "completed": False
    }

    response = requests.put(url, doc3)
    if (response.status_code > 199):
        print(response.json())


# usin gpath can update only one field
def using_patch():
    url = "https://jsonplaceholder.typicode.com/todos/20"

    doc4 = {
        "title": "submit ca1",
    }

    response = requests.patch(url, doc4)
    if (response.status_code > 199):
        print(response.status_code)
        print(response.json())


def currency_conversation():
    url = "https://v6.exchangerate-api.com/v6/0f215802f0c83392e64ee40d/pair"

    try:
        ans = 'y'
        while (ans == 'y'):
            val1 = input("enter first currency value: (e.g EUR) ")
            val2 = input("enter the second currency value: ")
            val = f"{val1}/{val2}"

            url1 = url+val
            data = requests.get(url1).json()
            result = data['convertion_rate']

            print(f"conversation rate {val1} to {val2} is {result}")

    except Exception as e:
        print(e)


def google_map_api():
    geo_locator = nt(user_agent="geoapiExcercises")

    place1 = "London"
    location1 = geo_locator.geocode(place1)

    user_map1 = folium.Map(location=[location1.latitude, location1.longitude])

    folium.Marker([location1.latitude, location1.longitude]).add_to(user_map1)

    place2 = "Dubai"
    location2 = geo_locator.geocode(place2)

    user_map2 = folium.Map(location=[location2.latitude, location2.longitude])

    folium.Marker([location2.latitude, location2.longitude]).add_to(user_map2)
    user_map1.show_in_browser()
    user_map2.show_in_browser()


def main():
    # post_method()
    # todo_posts()
    # using_put()
    # using_patch()
    # currency_conversation()
    google_map_api()


if __name__ == "__main__":
    main()
