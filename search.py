import re
import requests
from urllib import parse
from selenium import webdriver
from bs4 import BeautifulSoup as BS
from kyobo import chk_stock as KB
from yp import chk_stock as YP

def book_info(soup):
    info = {}
    con = soup.find('div', {'class':'book_info'})
    inner = soup.select('.book_info_inner > div')[1]
    info['title'] = con.select_one('h2 > a').text
    info['img'] = con.select_one('.thumb_type img')['src']
    info['auth'] = inner.select('a')[0].text
    info['pub'] = inner.select('a')[1].text
    bID = soup.select_one('.book_info_inner')
    p = re.compile("\d{13}") # isbn은 숫자 13자리
    info['isbn'] = (p.findall(bID.text))[0]
    return info

# def get_store_url(name):
#     s_url = soup.find('a', string=name)['href']
#     driver.get(s_url)

def select_store(num):
    if num == '1':
        # 교보문고는 책의 ISBN을 이용해 URL 주소 생성
        # 책의 ISBN 받아오기
        binfo = book_info(soup)
        bID = binfo['isbn']
        # 교보문고는 책 재고 페이지가 따로 존재
        # 추출한 ISBN을 이용해 URL로 바로 크롤링
        s_url = 'http://www.kyobobook.co.kr/prom/2013/general/StoreStockTable.jsp?barcode=' + bID + '&ejkgb=KOR'
        req = requests.get(s_url)
        store = BS(req.text, 'html.parser')
        print(KB(store))
    elif num == '2':
        s_url = soup.find('a', string='영풍문고')['href']
        req = requests.get(s_url)
        store = BS(req.text, 'html.parser')
        print(YP(store))
    elif num == '3':
        s_url = soup.find('a', string='반디앤루니스')['href']
        req = requests.get(s_url)
        s = BS(req.text, 'html.parser')
        store = s.select('.commTable_s th')
        num = s.select('.commTable_s a')
        stock = {}
        for i, j in zip(store[1:], num):
            stock[i.text] = j.text
        print(stock)

def search_engine(txt):
    # 네이버 도서에서 해당 책 검색하는 URL
    url = 'https://book.naver.com/search/search.nhn?sm=sta_hty.book&sug=&where=nexearch&query=' + txt
    driver.get(url)
    # 첫번째 검색된 책의 url 추출
    b_url = driver.find_element_by_xpath('//*[@id="searchBiblioList"]/li[1]/dl/dt/a').get_attribute('href')
    driver.get(b_url)
    soup = BS(driver.page_source, 'html.parser')
    driver.quit()
    return soup


# headless 위한 옵션 설정
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument('disable-gpu')

driver = webdriver.Chrome(r'C:\Users\smddu\Documents\chromedriver\chromedriver.exe', chrome_options=options)

txt = input('도서명을 입력하세요 : ')
soup = search_engine(txt)

# a = book_info(soup)
# print(a)
shop = input('도서 재고를 확인할 서점의 번호를 선택하세요(1.교보문고 2.영풍문고 3.반디앤루니스) : ')
select_store(shop)

while True:    
    sel = input("다른 서점의 재고를 확인하시려면 1, 종료하시려면 2를 입력해주세요. : ")
    if sel == '1':
        shop = input('도서 재고를 확인할 서점의 번호를 선택하세요(1.교보문고 2.영풍문고 3.반디앤루니스) : ')
        select_store(shop)
    elif sel == '2':
        break