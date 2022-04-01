# Import Required Library
import requests
from bs4 import BeautifulSoup
  
# Web URL
web_url = "https://www.dsebd.org/"
  
# get HTML content
html = requests.get(web_url).content
  
# parse HTML Content
soup = BeautifulSoup(html, "html.parser")
  
print(soup)
# js_files = []
# cs_files = []
  
# for script in soup.find_all("script"):
#     if script.attrs.get("src"):
          
#         # if the tag has the attribute 
#         # 'src'
#         url = script.attrs.get("src")
#         js_files.append(web_url+url)
  
  
# for css in soup.find_all("link"):
#     if css.attrs.get("href"):
          
#         # if the link tag has the 'href' 
#         # attribute
#         _url = css.attrs.get("href")
#         cs_files.append(web_url+_url)
  
# print(f"Total {len(js_files)} javascript files found")
# print(f"Total {len(cs_files)} CSS files found")

# for i in js_files:
#     print(i)