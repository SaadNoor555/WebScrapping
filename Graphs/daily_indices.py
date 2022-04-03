# done

from inspect import modulesbyfile
import requests
from bs4 import BeautifulSoup
  
def extract_time(date):
    # print(date)
    n_date, time = date.split(' ')
    new_time = ""
    return time

def extract_data(data):
    new_data = ""
    for i in data:
        if i=='.' or (i<='9' and i>='0'):
            new_data+=i
    return new_data

def get_data_from_market(pageData, st):
    datapoints = list()
    # print(type(pageData))
    flag = False
    for line in pageData.split('\n'):
        if line.find("var index_value_"+st+" = ") != -1:
            flag = True
            # print(line)
            # continue
        if flag:
            # print('yo')
            for data in line.split('\"+\"'):
                # print(data)
                datapoints.append(data)
            break

    # print(datapoints)
    mydata = list()
    for i in range(1, len(datapoints)):
        time, t_data = datapoints[i].split(',')
        # time = time[:-1]
        time = extract_time(time)
        t_data = float(extract_data(t_data))
        mydata.append([time, t_data])
    return mydata

def daily_indices(market):
    web_url = "https://www.dsebd.org/"
    html = requests.get(web_url).content
    soup = BeautifulSoup(html, "html.parser")
    # print(soup)
    market_data = get_data_from_market(str(soup), market)

    return market_data

    

print(daily_indices("ds30"))