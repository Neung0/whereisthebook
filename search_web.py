import re
import requests
from urllib import parse
from selenium import webdriver
from bs4 import BeautifulSoup as BS
from kyobo import chk_stock as KB
from yp import chk_stock as YP

def select_store(num):
    # 교보문고는 책의 ISBN을 이용해 URL 주소 생성
    # 책의 ISBN을 받아오기
    try :
        s_url = soup.find('a', string='인터넷 교보문고')['href']
        p = re.compile("\d{13}")
        bID = (p.findall(s_url))
        # 교보문고는 책 재고체크 페이지가 따로 존재하므로, 추출한 ISBN을 이용해 접속
        driver.get(
            'http://www.kyobobook.co.kr/prom/2013/general/StoreStockTable.jsp?barcode=' + bID[0] + '&ejkgb=KOR')
        store = BS(driver.page_source, 'html.parser')
        print(KB(store))
    except :
        print("재고없음")    

    try:
        s_url = soup.find('a', string='반디앤루니스')['href']
        req = requests.get(s_url)
        s = BS(req.text, 'html.parser')
        print(YP(store))
    except :
        print("재고없음")

    try:
        s_url = soup.find('a', string='반디앤루니스')['href']
        req = requests.get(s_url)
        s = BS(req.text, 'html.parser')
        store = s.select('.commTable_s th')
        num = s.select('.commTable_s a')
        stock = {}
        for i, j in zip(store[1:], num):
            stock[i.text] = j.text
        print(stock)
    except:
        print("재고없음")

def search_engine(txt):
    # 네이버 도서에서 해당 책 검색하는 URL
    url = 'https://book.naver.com/search/search.nhn?sm=sta_hty.book&sug=&where=nexearch&query=' + txt
    driver.get(url)
    # 첫번째 검색된 책의 url 추출
    b_url = driver.find_element_by_xpath('//*[@id="searchBiblioList"]/li[1]/dl/dt/a').get_attribute('href')
    driver.get(b_url)
    soup = BS(driver.page_source, 'html.parser')
    return soup


# headless 위한 옵션 설정
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument('disable-gpu')
driver = webdriver.Chrome(r'C:\Users\smddu\Documents\chromedriver\chromedriver.exe', chrome_options=options)

# txt = input('도서명을 입력하세요 : ')
soup = search_engine(txt)

shop = input('도서 재고를 확인할 서점의 번호를 선택하세요(1.교보문고 2.영풍문고 3.반디앤루니스) : ')
select_store(shop)
