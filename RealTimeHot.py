# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import pymongo

client = pymongo.MongoClient('localhost',27017)
mydb = client['mydb']
test = mydb['test']

headers = {
     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like 09	Gecko) Chrome/55.0.2883.87 Safari/537.36'
 }
info = []
url_1 = 'https://s.weibo.com/top/summary?cate=realtimehot'
url_2 = []
res = requests.get(url_1,headers=headers)
soup = BeautifulSoup(res.text,'html.parser')
infs = soup.select('#pl_top_realtimehot > table > tbody > tr > td > a')
ranks = soup.select('#pl_top_realtimehot > table > tbody > tr > td.ranktop')
links = soup.select('#pl_top_realtimehot > table > tbody > tr > td > a')
amounts = soup.select('#pl_top_realtimehot > table > tbody > tr > td > span')
for inf, rank, link,amount in zip(infs,ranks,links,amounts):
        data = {
            'inf':inf.get_text(),
            'rank':rank.get_text(),
            'amount': amount.get_text(),
            'link':'https://s.weibo.com'+link.get("href")
        }
        if data in info:
            pass
        else:
            info.append(data)
            test.insert_one(data)

