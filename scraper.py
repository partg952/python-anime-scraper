import requests
from bs4 import BeautifulSoup;


while True:
    keyword = input("Enter the name of the anime you want to search : ")
    if(len(keyword)==0):
        pass
    else:
        break;    
url_to_be_scraped = '';
request = requests.get("https://gogoanime2.org/search/"+keyword)
soup = BeautifulSoup(request.content,'html.parser')
divs = soup.find_all("p",class_="name");



def get_ep_url(url):
    ep_page_deatils = requests.get("https://gogoanime2.org"+url)
    ep_page = BeautifulSoup(ep_page_deatils.content,'html.parser');
    player_div = ep_page.find_all("div",class_="play-video");
    for items in player_div:
        iframe = items.find("iframe");
        print("Episode URL : "+iframe['src']);



def get_result(divs):
    num = 1
    for div in divs:
        title = div.find("a")
        print(num,"."+title['title'])
        num = num+1


get_result(divs);




if len(divs) != 0:
    index = int(input("Enter the index of the title : "))
    selected_title = divs[index-1];

    print("title selected : "+selected_title.a.string)
    url_to_be_scraped = selected_title.a['href']
    if len(url_to_be_scraped) != 0:
        anime_detail = requests.get("https://gogoanime2.org"+url_to_be_scraped)
        details = BeautifulSoup(anime_detail.content,'html.parser')
        ep_list = details.find('ul',id="episode_related")
        for ep in ep_list:
            a = ep.find("div")
            if a != -1:
                print(a.get_text())
            else:
                pass
        ep_index = int(input("Enter the episode number : "));
        ep_url = ep_list.find_all("li")[ep_index-1].a['href']
        get_ep_url(ep_url);
else:
    print("no results found!")    




