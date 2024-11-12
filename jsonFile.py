# this file regardin with json
import json
import pandas as pd
# loads() method parses a json string and returns list as a python dict

fname = "C:\\Users\\tahmm\\OneDrive - Dublin Business School (DBS)\\developments\\adv programming\\pythons\\dublinForecast.json"


def loadsFromStrig():
    input = '''
    [
        {
            "topic": "Databases", "name": "hentry korth", "bookname": "database system concepts"
        }, {
            "topic": "programming", "name": "charles severence", "bookname": "python for informatics"

        }, {
            "topic": "programming", "name": "christian negal", "bookname": "c# and .net"

        }, {
            "topic": "software engineering", "name": "roger pressman", "bookname": "software enigneering and practioners approaches"

        }
    ]
    '''

    try:
        info = json.loads(input)
        # print(f"No. of authors = {len(info)}")

    except Exception as e:
        print(f'An exception occurred {e}')

    for item in info:
        print(item)

    for item in info:
        print(f"\n topic: {item['topic']}")
        print(f"\n name: {item['name']}")
        print(f"\n bookname: {item['bookname']}")


# working with json formatted data set
# parsing a json file
# method: load
def loadFromJson():
    # fname = "C:\\Users\\tahmm\\OneDrive - Dublin Business School (DBS)\\developments\\adv programming\\pythons\\dublinForecast.json"
    try:
        with open(fname, 'r') as f:
            weatherData = json.load(f)
            if 'forecasts' in weatherData:
                for item in weatherData['forecasts']:
                    print(item)
            else:
                print("there is no forecasts data")
    except Exception as e:
        print(f"an error occured {e}")


# read with pandas

def loadfromJsonWithPandas():
    try:
        with open(fname, 'r') as f:
            weatherData = pd.read_json(f)
            # if 'forecasts' in weatherData:
            for item in weatherData['forecasts']:
                print(item)
                # forecasts_df = pd.DataFrame(weatherData['forecasts'].tolist())
                # print(forecasts_df)

            else:
                print("there is no forecasts data")

            print(forecasts_df)
    except Exception as e:
        print(f"an error occured {e}")


def asDataFrame():
    df = pd.read_json(fname)

    # print(df)
    for item in df['forecasts']:
        print(item)


def dumpsFrom():

    book1 = {
        "name": "java",
        "publication": "oracle press",
        "edition": 11,
        "year": 2023,
        "authors": ["herbert schildt", "danny coward"]
    }

    try:
        with open("BookData.json", 'w') as f:  # file mode is set to append write
            json.dump(book1, f)                # use dump to serialize
            print("file is created")

        print("---------------- book data.json")
        with open("BookData.json", 'r') as f:
            text = json.load(f)
            print(text)

        book2 = {
            "name": "python",
            "publication": "oracle press",
            "edition": 11,
            "year": 2023,
            "authors": ["herbert schildt", "danny coward"]
        }

        with open("BookData.json", 'a') as f1:
            json.dump(book2, f1)
            print("file is updated")
    except Exception as e:
        print(f"file operation failed {e}")


def main():
    # loadsFromStrig()
    # loadFromJson()
    # loadfromJsonWithPandas()
    # asDataFrame()
    dumpsFrom()


main()
