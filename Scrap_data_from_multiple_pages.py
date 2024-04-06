import requests
from bs4 import BeautifulSoup

#when the multiple link is similar 
for i in range(2,15):
    url = "https://www.flipkart.com/search?q=mobile+under+25000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY&page=" + str(i)
    # url = "https://www.flipkart.com/search?q=mobile%20under%2025000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)
    r = requests.get(url)
    # print(r)
    soup = BeautifulSoup(r.text,"lxml")
    # np --> next page, cnp --> complete next page
    np  = soup.find("a",class_ = "_1LKTO3").get("href")
    
    cnp = "https://www.flipkart.com"+np
    print(cnp)

# when our every next link is different than use while loop for our np (put all in while loop from np to soup)


# Example for not similler link 
# url = "https://www.flipkart.com/search?q=mobile+under+25000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY&page="
# r = requests.get(url)
# print(r)
# soup = BeautifulSoup(r.text,"lxml")
# while True:
#     np  = soup.find("a",class_ = "_1LKTO3").get("href")
#     cnp = "https://www.flipkart.com"+np
#     print(cnp)
#     url = cnp
#     r = requests.get(url)
#     soup = BeautifulSoup(r.text,"lxml")
