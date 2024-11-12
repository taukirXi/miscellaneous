# using urlib3

import urllib3


def withUrllib3():
    url = "https://en.wikipedia.org/wiki/Dublin"
    try:
        response = urllib3.request("GET", url)
        print(response.status)
        print(response.data)
    except:
        print('An exception occurred')


def withRequest():
    pass


