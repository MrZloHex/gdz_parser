import parser
import data

print("control")


def parse():
    for i in range(1, 12):
        for k in data.lessons:
            url = f'https://12baliv.com.ua/{i}-klas/{k}'
            parser.parsing(url, i, k)
