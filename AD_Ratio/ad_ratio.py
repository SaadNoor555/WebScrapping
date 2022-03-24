from  bs4 import BeautifulSoup
import requests

def count_ad_ratio():
    url = "https://www.dsebd.org/market-statistics.php"
    pages = requests.get(url)
    pages.text
    pageData = str(BeautifulSoup(pages.text, 'lxml'))
    flag = False
    for line in pageData.split('\n'):
        if line.find('All Category') != -1:
            flag = True
        if flag and line.find('ISSUES ADVANCED') != -1:
            ad_issue = line
        elif flag and line.find('ISSUES DECLINED') != -1:
            dc_issue = line
            break
    
    ad_num = [int(s) for s in str.split(ad_issue) if s.isdigit()]
    dc_num = [int(s) for s in str.split(dc_issue) if s.isdigit()]
    return ad_num[0]/dc_num[0]
    
    

print(count_ad_ratio())