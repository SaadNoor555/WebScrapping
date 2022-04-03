# done

from  bs4 import BeautifulSoup
import requests

def count_specific_ad_ratio(cat):
    url = "https://www.dsebd.org/market-statistics.php"
    pages = requests.get(url)
    pages.text
    pageData = str(BeautifulSoup(pages.text, 'lxml'))
    flag = False
    for line in pageData.split('\n'):
        if line.find(cat+' Category') != -1:
            flag = True
        if flag and line.find('ISSUES ADVANCED') != -1:
            ad_issue = line
        elif flag and line.find('ISSUES DECLINED') != -1:
            dc_issue = line
            break
    
    ad_num = [int(s) for s in str.split(ad_issue) if s.isdigit()]
    dc_num = [int(s) for s in str.split(dc_issue) if s.isdigit()]
    if dc_num[0]: ad_ratio = ad_num[0]/dc_num[0]
    else: ad_ratio = min(1, ad_num[0])
    return ad_ratio

def count_all_ad_ratio():
    ad_ratios = list()
    ad_ratios.append(count_specific_ad_ratio('All'))
    ad_ratios.append(count_specific_ad_ratio('A'))
    ad_ratios.append(count_specific_ad_ratio('B'))
    ad_ratios.append(count_specific_ad_ratio('N'))
    ad_ratios.append(count_specific_ad_ratio('Z'))
    return ad_ratios

print(count_all_ad_ratio())