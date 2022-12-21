
# HTTP - 하이퍼테긋트(html)을 전송하기위한 프로토콜
# 프로토콜 - 약속, 규약 ->
# url - http://www.naver.com
# uri - url에 사용자 정보와 스키마를 포함한값

# 스크래핑 - 웹페이지에서 자동으로 데이터를 추출하는것, 웹페이지 소유자의 허락없이
          # 무단으로 끌어오는 행위   
# 크롤링 - 웹페이지에서 자동으로 데이터 추출
# 스크래핑은 특정 웹사이트에서 데이터 추출, 크롤링은 웹사이트의 링크를통해서 정보를
# 찾아서 추출하는 방식
# 둘다 데이터 추출한다라는 것이 동일하기에 흔히 크롤링이라고 한다.

# 원하는 데이터만 뽑아오는것 - 파싱(parsing)

# import urllib.request
# import requests

from urllib.request import urlopen
import bs4

# test_html = "<html><head></head><body><div>hahahaha</div>"
# test_html += " <p>kjy babo</p> </body></html>"

# bobj = bs4.BeautifulSoup(test_html,"html.parser")

# print(test_html)
# print(bobj)

# print(test_html.find("div"))
# print(bobj.find("div"))
# print(bobj.find("p"))

# url = "https://www.naver.com"
# html = urlopen(url)

# print(html.read())
"""
html = 
<html>
    <body>
        <div>
            <ul class="kjy">
                <li>babo</li>
                <li>19</li>
            </ul>
            <ul class="ljh">
                <li>old mai...</li>
                <li>old...</li>
            </ul>
        </div>
    </body>
</html>
"""
# bsp = bs4.BeautifulSoup(html, "html.parser")

# 태그의 속성을 통해서 가져오는 방법
# ul = bsp.find("ul",{"class":"ljh"})
# print(ul['class'])

# li = bsp.findAll("li")
# print( li[1] )
# for i in li:
#     print(i.text)

url = "https://www.naver.com"
html = urlopen(url)
html = html.read()

bsp = bs4.BeautifulSoup(html, "html.parser")
temp = bsp.findAll("strong",{"class","current"})
print(temp[0].text)
for t in temp:
    if "현재기온" in t:
        print(t.txt)

# print(html)

"""
- HTTP(HTTPS -> SSL/TLS)[HTML과 JS와 CSS같은 파일을 웹 서버에게 요청하고 받아오는 프로토콜]
- HTML
- Javascript
- CSS
- ASP/ASP.NET ─┐
- JSP(JAVA)   ─│ -> 웹 서버 페이지를 만드는 기술들
- PHP         ─┘
- DB
"""                                                                            # 필수
# ======================================================================================
"""                                                                            # 선택
- Python
- Spring
- Jquery
- Ajax
"""
