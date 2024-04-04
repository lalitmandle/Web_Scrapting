import requests 
from bs4 import BeautifulSoup
url = "https://webscraper.io/test-sites/e-commerce/allinone/computers"
r = requests.get(url)
# print(r.status_code)
# print(r.text)
soup = BeautifulSoup(r.text,'lxml')
tag = soup.header 
print(tag.attrs)