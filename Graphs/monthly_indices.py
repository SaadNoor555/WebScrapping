# done

from  bs4 import BeautifulSoup
import requests

def extract_date(date):
    new_date = ""
    for i in date:
        if i=='-' or (i<='9' and i>='0'):
            new_date+=i
    return new_date

def extract_data(data):
    new_data = ""
    for i in data:
        if i=='.' or (i<='9' and i>='0'):
            new_data+=i
    return new_data

def get_data(market):
    url = "https://dsebd.org/php_graph/monthly_graph_index.php?type="+market+"&duration=1"
    pages = requests.get(url)
    pages.text
    pageData = str(BeautifulSoup(pages.text, 'lxml'))
    flag = False
    datapoints = list()
    for line in pageData.split('\n'):
        if line.find("Date,"+market.upper()+" Index") != -1:
            flag = True
        elif flag:
            for data in line.split('\"+\"'):
                datapoints.append(data)
            break

    tot_datapoints = len(datapoints)
    first_day_data = datapoints[0]
    last_day_data = datapoints[tot_datapoints-1]
    last_day_data = last_day_data[:-2]
    # print(last_day_data)
    first_day, first_data = first_day_data.split(',')
    last_day, last_data = last_day_data.split(',')
    
    first_data, last_data = float(extract_data(first_data)), float(extract_data(last_data))
    indices = [first_data, last_data, last_data-first_data, (last_data-first_data)*100/first_data]
    '''first , last, change, change(%)'''
    return indices
    
    

list = get_data("cdset")
print(list)
