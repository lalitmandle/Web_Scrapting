#With the help of pandas we create data frame here and that data frame you can store that data frame inside the CSV file or an Excel sheet.
import pandas as pd
import requests
from bs4 import BeautifulSoup
url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r = requests.get(url)
soup = BeautifulSoup(r.text,"lxml")
name = soup.find_all("a",class_ = "title")
# print(name)
product_name = []
for i in name:
    name = i.text
    product_name.append(name)
# print(product_name)

prices = soup.find_all("h4",class_ = "float-end price card-title pull-right")
product_prices = []
for i in prices:
    price = i.text
    product_prices.append(price)
# print(product_prices)

desc = soup.find_all("p",class_ = "description")
desc_list = []
for i in desc:
    des = i.text
    desc_list.append(des)
# print(desc_list)
    
reviews = soup.find_all("p",class_ = "float-end review-count")
review_list = []
for i in reviews:
    review = i.text
    review_list.append(review)
# print(review_list)

#create data frame
df = pd.DataFrame({"Product Name":product_name, "Prices":product_prices,"Descriptions":desc_list,"Number of reviews":review_list})
# print(df)

#add it inside of excel file 
df.to_csv("products_details.csv")