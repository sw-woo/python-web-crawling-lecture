import os, re, csv
import requests
import urllib.request as ur
from bs4 import BeautifulSoup as bs
url = 'http://quotes.toscrape.com/'

html = ur.urlopen(url)

# print(html)
# print(html.read()[:100])


soup = bs(html.read(), 'html.parser')

# print(soup)

# type_soup = type(soup)
# type_html = type(html)

# print(f'html 타입 객체 {type_html}')

# print(f'soup 타입 객체 {type_html}')


 
# quote = soup.find_all('span')

# print(quote[0])
# print('--------------------------')
# print(quote[0].text)


# print('--------------------------')


# span 태그 텍스트 반복 출력
# for i in quote:
#     print(i.text)


# print(soup.find_all('div',{"class":"quote"})[0].text)

for i in soup.find_all('div',{"class":"quote"}):
    print(i.text)


#다음 기사 제목, 본문, 하이퍼링크를 파일로 저장하기

url = 'https://news.daum.net/'

os.chdir(r'/Users/usermackbookpro/web-python-crawling')

soup = bs(ur.urlopen(url).read(),'html.parser')

f = open('article_total.txt','w', encoding='utf8')

for i in soup.find_all('div',{"class":"item_issue"}):
    try:
        # 예외처리를 사용합니다. 
        f.write(i.text + '\n')
        #제목을 추출해서 파일에 씁니다. 

        f.write(i.find_all('a')[0].get('href')+'\n')
        #url 주소를 추출해 파일에 씁니다. 

        soup2 = bs(ur.urlopen(i.find_all('a')[0].get('href')).read(),'html.parser')
        #URL 주소에 해당하는 웹 문서를 열어 새 뷰티풀수프로 객체로 저장합니다.

        for j in soup2.find_all('p'):
            f.write(j.text)
    except:
        pass

f.close()




















