import requests
import bs4
import urllib
from urllib.request import urlopen
import pymysql


#데이터 베이스 연결
conn = pymysql.connect(host ='127.0.0.1', user='root', password = 'cyd68400', db='dw_501',charset='utf8')
#데이터베이스 연결 후에 커서 생성, 커서는 파이썬과 DB 사이를 연결해주는 드라이버의 형태
#커서생성
cur = conn.cursor()

# 쇼핑몰에서 이름 가져오기
url = "https://weather.naver.com/today/07140102?cpName=KMA"
#res = requests.get(url =url)
html = urlopen(url)

bsp = bs4.BeautifulSoup(html,"html.parser")
href_list= []
items = bsp.findAll("div",{"class","weader_area"})
for item in items:
    href_list.append( item.find("a")['href'])
    print(item)