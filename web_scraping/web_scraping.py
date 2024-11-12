from urllib.request import urlopen
# using the urllib.requst 

def openWebsite():
    url = "https://en.wikipedia.org/wiki/Dublin"

    try:
        page = urlopen(url)
        for line in page:
            print(line)

    except Exception as e:
        print(f"operation faild {e}")


openWebsite()
