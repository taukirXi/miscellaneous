import csv
import pandas as pd

# load csv file from pc


def loadCsv():
    try:
        # with open(r"C:\\Users\\tahmm\\OneDrive - Dublin Business School (DBS)\developments\\adv programming\\pythons\\user_behavior_dataset.csv", "r") as fhand:
        with open("C:\\Users\\tahmm\\OneDrive - Dublin Business School (DBS)\developments\\adv programming\\pythons\\user_behavior_dataset.csv", "r") as fhand:
            text = csv.reader(fhand, delimiter=",")
            print(text)
            for item in text:
                print(item)

    except FileNotFoundError:
        print("file not found....")
        print("program will terminate now.....")


# fetch first 100 rows

def loadCsvLoad100Data():
    try:
        # with open(r"C:\\Users\\tahmm\\OneDrive - Dublin Business School (DBS)\developments\\adv programming\\pythons\\user_behavior_dataset.csv", "r") as fhand:
        with open("C:\\Users\\tahmm\\OneDrive - Dublin Business School (DBS)\developments\\adv programming\\pythons\\user_behavior_dataset.csv", "r") as fhand:
            text = csv.reader(fhand, delimiter=",")
            # print(type(text))
            # for item in text:
            #     print(item)
            rows = list(text)
            for item in rows[:100+1]:
                print(item)

    except FileNotFoundError:
        print("file not found....")
        print("program will terminate now.....")


# write vlues into csv file
# this is put values into a csv file by creatig it

def writeCsvFile():

    heading = ["player name", "sports", "age", "country"]
    rows = [["roger federer", "tennis", 40, "swiss"],
            ["sachin tendulkar", "cricket", 50, "india"],
            ["serena williams", "tennis", 38, "us"],
            ["evan ferguson", "football", 25, "ireland"],
            ["troy parrott", "tennis", 32, "ireland"]
            ]

    fname = "players.csv"

    try:
        with open(fname, 'w') as fhand:
            csv_writer = csv.writer(fhand)
            csv_writer.writerow(heading)
            csv_writer.writerows(rows)
        print("file players.cvs if ready....")
    except:
        print("file operation failed.")
        print("program will be terminating now....")

# working with dict


def dictToCsv():
    authors = [
        {
            'topic': 'Databases', 'name': 'hentry korth', 'bookname': 'database system concepts'
        }, {
            'topic': 'programming', 'name': 'charles severence', 'bookname': 'python for informatics'

        }, {
            'topic': 'programming', 'name': 'christian negal', 'bookname': 'c# and .net'

        }, {
            'topic': 'software engineering', 'name': 'roger pressman', 'bookname': 'software enigneering and practioners approaches'

        }


    ]

    fields = ['topic', 'name', 'bookname']
    fname = "authors.csv"

    # try:
    #     #   with open(fname, 'w') as fhand:
    #     fhand = open(fname, 'w')
    #     writer = csv.DictWriter(fhand, fieldnames=fields)
    #     writer.writeheader()
    #     writer.writerows(authors)
    #     print("file is ready")
    # except:
    #     print("file operation failed... \n program will be termniating....")
    # finally:
    #     fhand.close()
    #     print("file is closed")

    try:
        with open(fname, 'w') as fhand:
            writer = csv.DictWriter(fhand, fieldnames=fields)
            writer.writeheader()
            writer.writerows(authors)
            print("file authors.csv is ready.....")
    except Exception as e:
        print(f'An exception occurred {e}')

# load file with pandas


def pandaLoadFile():
    try:
        df = pd.read_csv(
            "C:\\Users\\tahmm\\OneDrive - Dublin Business School (DBS)\developments\\adv programming\\pythons\\user_behavior_dataset.csv")
        print(df)

    except:
        print("faild to load")

# with pandas fetch first 100


def pandaFetchFirst100():
    try:
        df = pd.read_csv(
            "C:\\Users\\tahmm\\OneDrive - Dublin Business School (DBS)\developments\\adv programming\\pythons\\user_behavior_dataset.csv")
        # print(df)

        # conventional method not work
        # only prints header

        # print(type(df))
        # rows = list(df)
        # for item in rows[:100+1]:
        #     print(item)

        print(df.head(100+1))

    except:
        print("faild to load first 100")


def main():
    # loadCsv()
    # writeCsvFile()
    # loadCsvLoad100Data()
    # dictToCsv()
    # pandaLoadFile()
    pandaFetchFirst100()


main()
