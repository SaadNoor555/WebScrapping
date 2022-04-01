from  bs4 import BeautifulSoup
import requests

def get_data():
    url = "https://www.dsebd.org/"
    pages = requests.get(url)
    pages.text
    pageData = str(BeautifulSoup(pages.text, 'lxml'))
    # file = open("dse.txt", "w+")
    # for i in pageData:
    #     file.write(i)
    # file.close()
    return pageData
    # flag = False
    # for line in pageData.split('\n'):
    #     if line.find('All Category') != -1:
    #         flag = True
    #     if flag and line.find('ISSUES ADVANCED') != -1:
    #         ad_issue = line
    #     elif flag and line.find('ISSUES DECLINED') != -1:
    #         dc_issue = line
    #         break
    
    # ad_num = [int(s) for s in str.split(ad_issue) if s.isdigit()]
    # dc_num = [int(s) for s in str.split(dc_issue) if s.isdigit()]
    # return ad_num[0]/dc_num[0]
    
    

print(get_data())