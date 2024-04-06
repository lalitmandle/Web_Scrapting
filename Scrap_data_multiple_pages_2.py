# How extract data from one page
import requests
from bs4 import BeautifulSoup
import pandas as pd

Names = []
Prices = []
Discount = []
Original_Price = []
Desc = []
Reviews = []

# When you want to all pages data then pass all code on for loop accept dataFrame and also change in the url str(1) to str(i)

# url = "https://www.flipkart.com/search?q=mobile+under+25000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY&page="+str(1)
# r = requests.get(url)
# print(r)

# soup = BeautifulSoup(r.text,"html.parser")
# box = soup.find('div',class_ = "_1YokD2 _3Mn1Gg")
# names = box.find_all('div', class_ = "_4rR01T")
# print(names)
# for i in names:
#     n = i.text
#     Names.append(n)
# print(len(Names))

# #for prices
# prices = box.find_all('div',class_ = "_30jeq3 _1_WHN1")
# for i in prices:
#     Prices.append(i.text)
# print(len(Prices))

# #for discount
# disc = box.find_all('div',class_ = "_3Ay6Sb")
# for i in disc:
#     Discount.append(i.text)
# print(len(Discount))

# # Original prices
# op = box.find_all('div',class_ = "_3I9_wc _27UcVY")
# for i in op:
#     Original_Price.append(i.text)
# print(len(Original_Price))

# #Discription 
# desc = box.find_all('ul',class_ = "_1xgFaf")
# for i in desc:
#     Desc.append(i.text)
# print(len(Desc))

# # Reviews
# rev = box.find_all('div',class_= "_3LWZlK")
# for i in rev:
#     Reviews.append(i.text)
# print(len(Reviews))


# #create Data Frame 
# df = pd.DataFrame({"Product Name":Names,"Original Price":Original_Price,"Discount":Discount,
#                    "Product Price":Prices,"Description":Desc,"Reviews":Reviews})
# # print(df)
# df.to_csv("Mobiles_under_25k.csv")


for i in range(0,4):
    url = "https://www.flipkart.com/search?q=mobile+under+25000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY&page="+str(i)
    r = requests.get(url)
    soup = BeautifulSoup(r.text,"html.parser")
    box = soup.find('div',class_ = "_1YokD2 _3Mn1Gg")
    names = box.find_all('div', class_ = "_4rR01T")
    print(names)
    for i in names:
        n = i.text
        Names.append(n)
    print(len(Names))

    #for prices
    prices = box.find_all('div',class_ = "_30jeq3 _1_WHN1")
    for i in prices:
        Prices.append(i.text)
    print(len(Prices))

    #for discount
    disc = box.find_all('div',class_ = "_3Ay6Sb")
    for i in disc:
        Discount.append(i.text)
    print(len(Discount))

    # Original prices
    op = box.find_all('div',class_ = "_3I9_wc _27UcVY")
    for i in op:
        Original_Price.append(i.text)
    print(len(Original_Price))

    #Discription 
    desc = box.find_all('ul',class_ = "_1xgFaf")
    for i in desc:
        Desc.append(i.text)
    print(len(Desc))

    # Reviews
    rev = box.find_all('div',class_= "_3LWZlK")
    for i in rev:
        Reviews.append(i.text)
    print(len(Reviews))


#create Data Frame 
df = pd.DataFrame({"Product Name":Names,"Original Price":Original_Price,"Discount":Discount,
                   "Product Price":Prices,"Description":Desc,"Reviews":Reviews})
# print(df)
df.to_csv("Mobiles_under_25k_all.csv")