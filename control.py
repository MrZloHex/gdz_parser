import parser
import data


# method of control URL and giving it to parse function
def parse():
    for i in range(1, 12):
        for k in data.lessons:
            url = f'https://12baliv.com.ua/{i}-klas/{k}'    # forming URL
            parser.parsing(url, i, k)                       # starting the parse process
