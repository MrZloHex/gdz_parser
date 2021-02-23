import bs4
import requests
import DB
import data
import re


# method of parsing data
def parsing(url: str, klass: int, lesson: str):
    resp = requests.get(url)
    soup = bs4.BeautifulSoup(resp.text, 'lxml')                             # connecting with bs4 to site

    div = soup.find_all('div', attrs={'class': 'book-box book-item'})       # finding all containers with data of book

    for each_div in div:                                                    # parsing data of each book
        # var of type and year of the book
        year = 0
        tip = ''

        # split container  for some useful parts
        h3 = re.split('<h3>', str(each_div))
        li = re.split('</strong>', str(each_div))
        img = re.split('"lazy" src="', str(each_div))

        # taking book's information
        name_book = re.split('</', h3[1])
        authors = re.split('</li>', li[1])
        kind = re.split('<strong>', li[1])
        img_src = re.split('"', img[1])

        # taking the year and type of book
        if kind[1] == 'Рік видання: ':
            y = re.split('</li>', li[2])
            year = int(y[0])
            tip = ''
        elif kind[1] == 'Тип: ':
            y = re.split('</li>', li[3])
            year = int(y[0])
            t = re.split('</li>', li[2])
            tip = t[0]

        # inserting all data in database
        DB.insert(klass, data.lesson[lesson], name_book[0], authors[0], tip, year, img_src[0])
