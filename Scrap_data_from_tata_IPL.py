import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.iplt20.com/auction/2022"
r = requests.get(url)
# print(r)
soup = BeautifulSoup(r.text,"lxml")
table = soup.find("table",class_ = "ih-td-tab auction-tbl")
# print(table)
headers = soup.find_all("th")
# print(headers)
titles = []
for i in headers[:4]:
    titles.append(i.text)
# print(titles)
df= pd.DataFrame(columns=titles)
# print(df)

rows = table.find_all("tr")
# for i in rows[1:]:
#     data = i.find_all("td")
#     # print(data)
#     row = [tr.text for tr in data]
#     # print(row)
#     l = len(df)
#     df.loc[l] = row
# df = df.replace('\n','',regex=True)
# print(df)
# df.to_csv("TATA_IPL_Auction_2022.csv")
for i in rows[1:]:
    first_td = i.find_all("td")[0].find("div",class_ = "ih-pt-ic").text.strip()#strip remove the all \n and replace that place by empty string
    data = i.find_all("td")[1:]
    # print(first_td)
    row = [tr.text for tr in data]
    row.insert(0,first_td)
    print(row)
    l = len(df)
    df.loc[l] = row
# df = df.replace('\n','',regex=True)
print(df)
df.to_csv("TATA_IPL_Auction_2022_1.csv")