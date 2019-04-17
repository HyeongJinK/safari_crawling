from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://programming.zz.am")
bsObject = BeautifulSoup(html, "html.parser")

#print(bsObject) # html 가져오기
print(bsObject.head.title) # 타이틀 가져오기

for meta in bsObject.head.find_all('meta'): # meta 데이터 가져오기
    print(meta.get('content'))

print(bsObject.head.find("meta", {"name":"description"}))
#print(bsObject.body.find("div"))