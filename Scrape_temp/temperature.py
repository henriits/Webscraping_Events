import requests
import selectorlib
from emailing import send_email
from datetime import datetime
import sqlite3

URL = "http://programmer100.pythonanywhere.com/"
HEADER = HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

connection = sqlite3.connect("tempdata.db")


def scrape(URL):
    """ Scrape the page source from URL"""
    response = requests.get(URL, headers=HEADERS)
    source = response.text
    return source




def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["value"]
    return value


def store(extracted):
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    cursor = connection.cursor()
    cursor.execute("INSERT INTO temperature_data VALUES(?,?)", (now, extracted))
    connection.commit()


if __name__ == "__main__":
    scraped = (scrape(URL))
    extracted = extract(scraped)
    print(extracted)
    store(extracted)
