import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://ticker.finology.in/"
r = requests.get(url)
# print(r)
soup = BeautifulSoup(r.text,"lxml")
table = soup.find("table",class_ = "table table-sm table-hover screenertable")
# print(table)
#for header 
headers = table.find_all("th")
titles = []
for i in headers:
    titles.append(i.text)

# print(titles)
#convert to dataframe
df = pd.DataFrame(columns=titles)
# print(df)
rows = table.find_all("tr")
# print(rows)
for i in rows[1:]:
    # print(i.text)
    data = i.find_all("td")
    # print(data)
    row = [tr.text for tr in data]
    # print(row)
    # append data to the dataframe
    l = len(df)
    df.loc[l] = row

df = df.replace('\n','', regex = True)   
# print(df)
df.to_csv("stock_market_data.csv")