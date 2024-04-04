import requests
from bs4 import BeautifulSoup
url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r = requests.get(url)
soup = BeautifulSoup(r.text,"lxml")

name = soup.find_all("a",class_ = "title")
print("2nd product name is : ",name[1].string)
prices = soup.find_all("h4",class_ = "float-end price card-title pull-right")
print("2nd item price is : ",prices[1].text)
desc = soup.find_all("p",class_ = "description")
print("2nd item description is : ",desc[1].string)
# print(len(prices))
# for i in prices:
#     print(i.text)