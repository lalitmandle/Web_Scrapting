import requests
from bs4 import BeautifulSoup
url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

r = requests.get(url)
# print(r)
soup = BeautifulSoup(r.text,"html.parser")
# print(soup.find('div'))
price = (soup.find("h4",{"class":"float-end price card-title pull-right"}))
print(price.string)
desc = soup.find("p",{"class":"description"})
print(desc.string)
print(soup.find("a",class_ = "title").string)