import os, codecs, re, datetime , requests

import urllib.request as ur

from bs4 import BeautifulSoup as bs 

#pip install pyinstaller 설치후 
#터미널에서 실행파일 만들기 pyinstaller --onefile [파이썬파일].py
# ex) pyinstaller --onefile article_collector.py
#성공후 dist폴더[디렉토리]에 실행 파일 실행 

os.chdir(r'/Users/usermackbookpro/web-python-crawling')

url = 'https://news.daum.net/'

f = open(str(datetime.date.today())+' article_total_master.txt','w', encoding='utf8')

soup = bs(ur.urlopen(url).read(),'html.parser')

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