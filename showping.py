import requests
import bs4
import urllib
from urllib.request import urlopen
import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='cyd68400',
db='dw_501', charset='utf-8')

cur = conn.cursor()

url = "https://www.graychic.co.kr/product/list.html?cate_no=4"
# res = requests.get(url=url)
html = urlopen(url)

bsp = bs4.BeautifulSoup(html, "html.parser")

href_list = []
items = bsp.findAll( "div",{"class","sp-product__thumb"} )
for item in items:
    href_list.append( item.find("a")['href'] )

site = "https://www.graychic.co.kr"

item_list = dict() # 제품의 상세 정보 저장 딕셔너리(key - 상품명, value - 정보)

for i in range(len(href_list)):
    href = urllib.parse.quote(href_list[i]) # 주소에 한글있으면 인코딩해서 사용
    item_link = site + href # 제품 상세페이지 주소

    item_html = urlopen(item_link) # 제품 상세페이지 html

    item_bsp = bs4.BeautifulSoup(item_html,"html.parser") # 제품 상세페이지 파서
    
    item_name = '' # 제품명
    info_t = item_bsp.select_one("#gc_de_sizeinfo")

    info_tr = info_t.select("tr")
    th_list = []
    td_list = []
    try:
        for tr in info_tr:
            try:
                th = tr.select_one ("th").text
                td = tr.select_one ("td").text
            except Exception as e: # 오류가 있다면 오류정보 E에 저장
                continue
            else:
                if '상품명' == th:
                    item_name = td
                else:
                    th_list.append(th)
                    td_list.append(td)
    except Exception as e:
        print( "몇번 째 제품 오류 : " + str(i) )

    size_t = item_bsp.select_one("#gc_de_sizecm")
    size_th = size_t.select("th")
    for th in size_th:
        th_list.append(th.text)
    size_td = size_t.select("td")
    for td in size_td:
        td_list.append(td.text)

# 윤도 바ㅏㅏㅏ보 멍충이ㅣㅣㅣㅣ 뚱돼지. 아조씨 담배냄새 난대요.. 그만피세요!!!🤬
    item_list[item_name] = dict(zip(th_list, td_list))
cur.execute( "insert into outers values('"+ a +"')" )
print(item_list)
    

# find -> html tag로 찾기 , select -> css 선택자
# fint -> 태그 1개, findAll -> 태그 여러개 , select -> 선택자에 해당되는 모든태그
# selectOne -> 1개 태그

# info_tr = info_t.findAll("tr")
# for tr in info_tr:
#     th = tr.find("th").text
#     td = tr.find("td").text
#     print( th , td )

# print(info_t)

# print( info_t )

# names = bsp.findAll("p",{"class","name"})

# price = bsp.findAll("span",{"class","p_value"})

# item = []
# for i in range(len(names)):
#     name = names[i].find("a").text
#     p = price[i].find("strong").text
#     item.append( [name, p] )
# print( item )
