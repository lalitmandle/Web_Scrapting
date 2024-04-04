import requests
import re
from bs4 import BeautifulSoup
url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r = requests.get(url)
soup = BeautifulSoup(r.text,"lxml")
# data = soup.find_all(["h4","a","p"])
# data1 = soup.find_all(string = "Galaxy Tab")
data = soup.find_all(string = re.compile("Galaxy"))
print(data)