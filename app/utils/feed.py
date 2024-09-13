import requests
# from xml.etree import ElementTree
from bs4 import BeautifulSoup
from .date_parser import parse_date



def feed_parser(rss_url: str) -> dict:
    response = requests.get(rss_url)
    
    data = []
    if response.status_code == 200:
        rss_feed = response.text
        soup = BeautifulSoup(rss_feed, features="xml")
        entries = soup.find_all('item')
        if len(entries) > 0:
             if not entries:
                 return []
             for item in entries:
                item_list = item.find_all()
                item_dict = {}
                for i in item_list:
                    if i.name == 'thumbnail':
                        img = i['url']
                        caption = i['caption']
                        item_dict.update({'caption': caption,'media': img})

                    item_dict.update({i.name: i.string})
                    if i.name == 'pubDate':
                         item_dict[i.name] = parse_date(item_dict[i.name])
                data.append(item_dict)
    data.sort(key=lambda x: x['pubDate'])
    return data
    

                     
                 
             
        