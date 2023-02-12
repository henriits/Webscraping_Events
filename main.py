import requests
import selectorlib
from emailing import send_email
from datetime import datetime
import sqlite3
import time

"INSERT INTO events VALUES ('Tigers', 'Tiger city','2088.10.14') "
"SELECT * FROM events WHERE date='2088.10.15'"

URL = "http://programmer100.pythonanywhere.com/tours/"
HEADER = HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

now = datetime.now()
datetime_string = now.strftime("%d/%m/%Y %H:%M:%S")

connection = sqlite3.connect("data.db")


def scrape(URL):
    """ Scrape the page source from URL"""
    response = requests.get(URL, headers=HEADERS)
    source = response.text
    return source


def read(extracted):
    row = extracted.split(",")
    row = [item.strip() for item in row]
    band, city, date = row
    cursor = connection.cursor()
    cursor.execute("SELECT band,date FROM events WHERE band=? AND city=? AND date=?", (band, city, date))
    rows = cursor.fetchall()
    print(rows)
    return rows


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["value"]
    # temperature = extractor.extract(source)["temperature"]
    return value


def store(extracted):
    with open("data.txt", "a") as file:
        file.write(datetime_string + "," + extracted + "\n")


if __name__ == "__main__":
    while True:  # with this program runs nonstop

        scraped = (scrape(URL))
        extracted = extract(scraped)
        print(extracted)
        store(extracted)

        if extracted != "No upcoming tours":
            row = read(extracted)
            if not row:
                store(extracted)
                send_email(message="Hey, new event was found!")
        time.sleep(2)  # runs every 2 seconds
