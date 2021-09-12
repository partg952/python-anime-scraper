import requests
from bs4 import BeautifulSoup;

keyword = input("Enter the name of the anime you want to seatch : ")
num = 1
request = requests.get("https://gogoanime.pe//search.html?keyword="+keyword)
soup = BeautifulSoup(request.content,'html.parser')
divs = soup.find_all("p",class_="name");
for div in divs:
    title = div.find("a")
    print(num,"."+title['title'])
    num = num+1