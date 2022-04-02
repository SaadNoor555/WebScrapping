# Import Required Library
import requests
from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup

def extract_adn_val(lines):
    values = list()
    for line in lines:
        line = line[:-6]
        val = ""
        i = len(line)-1
        while line[i]!='>':
            val = line[i] + val
            i-=1
        values.append(int(val))
    return values


def daily_adn():
    url = "https://www.dsebd.org/"
    pages = requests.get(url)
    pages.text
    pageData = str(BeautifulSoup(pages.text, 'lxml'))
    # print(pageData)
    skipLine = -100
    adn = list()
    for line in pageData.split('\n'):
        if line.find('Issues Advanced') != -1:
            skipLine = 5
        if skipLine <= 0 and skipLine >= -2:
            adn.append(line)
        if skipLine == -3:
            break
        if skipLine != -100:
            skipLine -=1

    advance, decline, nutral = extract_adn_val(adn)
    return advance, decline, nutral


print(daily_adn())