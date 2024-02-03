import os, re, csv
import requests
import urllib.request as ur
from bs4 import BeautifulSoup as bs


os.chdir(r'/Users/usermackbookpro/web-python-crawling')

news = 'https://news.daum.net/'

soup = bs(ur.urlopen(news).read(), 'html.parser')

# print(soup)

# item_soup = soup.find_all('div',{"class":"item_issue"})

# print(item_soup)

# 반복문으로 기사 제목 모두 추출하기

# for i in soup.find_all('div',{"class":"item_issue"}):
#     print(i.text)

# a태그만 추출 하기
# a_soup=soup.find_all('a')[:5]

# print(a_soup)


#get으로 href 속성값 구하기 

# a_list = []

# for i in soup.find_all('div',{"class":"item_issue"}):
#     a_tag = i.find_all('a')[0].get('href')
#     a_list.append(a_tag)

# print(a_list)


#다음 기사 제목과 내용 한꺼번에 추출하기 

# article1 = 'https://go.seoul.co.kr/news/newsView.php?id=20200427004004&wlog_%20tag3=daum'


# soup2 = bs(ur.urlopen(article1).read(),'html.parser')

# for i in soup2.find_all('p'):
#     print(i.text)



#기사 제목 가져오기 

headline = soup.find_all('div',{"class":"item_issue"})

# print(headline[0].text)


#하이퍼링크된 모든 기사의 제목과 본문 추출하기 

# for i in headline:
#     #headline 객체에서 <div> 태그를 하나씩 가져옵니다.
    
    
#     print(i.text, '\n')
#     #기사 제목을 출력합니다.

#     soup3 = bs(ur.urlopen(i.find_all('a')[0].get('href')).read(),'html.parser')
#     #해당 기사가 올라와 있는 웹 사이트를 열어 soup3 객체에 저장합니다.

#     for j in soup3.find_all('p'):
#         j.text
#     #<p> 태그에서 텍스트만 출력합니다.
        


# 다음 기사 url 주소 저장하기 

# os.chdir(r'/Users/usermackbookpro/web-python-crawling')

# f = open('link.txt','w')

# for i in soup.find_all('div',{"class":"item_issue"}):
#     f.write(i.find_all('a')[0].get('href')+'\n')

# f.close()



#다음 기사 본문을 파일로 저장하기 총 2개 실습해보기

# article1 = 'https://go.seoul.co.kr/news/newsView.php?id=20200427004004&wlog_%20tag3=daum'


# soup2 = bs(ur.urlopen(article1).read(),'html.parser')

# f = open('article_1.txt','w')

# for i in soup2.find_all('p'):
#     f.write(i.text)



article2 = 'https://v.daum.net/v/20240203112846851'


soup2 = bs(ur.urlopen(article2).read(),'html.parser')

f = open('article_2.txt','w')

for i in soup2.find_all('p'):
    f.write(i.text+'\n')

