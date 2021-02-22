import bs4
import requests
import DB
import data
import re


def parsing(url: str, klass: int, lesson: str):
    print("parser")
    resp = requests.get(url)

    soup = bs4.BeautifulSoup(resp.text, 'lxml')

    ul = soup.find_all('ul', attrs={'class': 'book-item-info'})

    for each_ul in ul:
        name_book = None

        li = each_ul.find_all('li')
        for each_li in li:
            test_name = each_li.find('h3')
            if test_name:
                name_book = each_li.find('h3').text

            DB.insert(klass, data.lesson[lesson], name_book)

            if name_book or name_book == "":
                break
