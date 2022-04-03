# Import Required Library
# done
import requests
from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup

def extract_tvt_val(line):
    values = list()

    val = ""
    for i in line:
        if i=='.' or (i>='0' and i<='9'):
            val += i
    return val

def daily_tvt():
    url = "https://www.dsebd.org/"
    pages = requests.get(url)
    pages.text
    pageData = str(BeautifulSoup(pages.text, 'lxml'))
    # print(pageData)
    skipLine = -100
    tvt = list()
    for line in pageData.split('\n'):
        if line.find('Total Trade') != -1:
            skipLine = 6
        if skipLine <= 0 and skipLine >= -4:
            if skipLine % 2 == 0:
                tvt.append(line)
        if skipLine == -5:
            break
        if skipLine != -100:
            skipLine -=1

    tot_trade = int(extract_tvt_val(tvt[0]))
    tot_volume = int(extract_tvt_val(tvt[1]))
    tot_value = float(extract_tvt_val(tvt[2]))

    return tot_trade, tot_volume, tot_value

print(daily_tvt())