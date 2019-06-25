import re
from urllib import parse
from selenium import webdriver
from bs4 import BeautifulSoup as BS
from kyobo import chk_stock as KB
from yp import chk_stock as YP

def select_store(name):
    s_url = soup.find('a', string = name)['href']
    driver.get(s_url)
    

txt = input('도서명을 입력하세요 : ')
# 네이버 도서에서 해당 책 검색하는 URL
url = 'https://book.naver.com/search/search.nhn?sm=sta_hty.book&sug=&where=nexearch&query=' + parse.quote(txt)
# headless 위한 옵션 설정
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument('disable-gpu')
driver = webdriver.Chrome(r'C:\Users\smddu\Documents\chromedriver\chromedriver.exe', chrome_options=options)
driver.get(url)
# 첫번째 검색결과의 url 추출
b_url = driver.find_element_by_xpath('//*[@id="searchBiblioList"]/li[1]/dl/dt/a').get_attribute('href')
driver.get(b_url)
soup = BS(driver.page_source, 'html.parser')

shop = input('도서 위치를 검색할 서점의 번호를 선택하세요(1.교보문고 2.영풍문고) : ')
if shop == '1':
    # 교보문고는 책의 ISBN을 이용해 URL 주소 생성
    # 책의 ISBN을 받아오기
    s_url = soup.find('a', string = '인터넷 교보문고')['href']
    p = re.compile("\d{13}")
    bID = (p.findall(s_url))
    # 교보문고는 책 재고체크 페이지가 따로 존재하므로, 추출한 ISBN을 이용해 접속
    driver.get('http://www.kyobobook.co.kr/prom/2013/general/StoreStockTable.jsp?barcode=' + bID[0] + '&ejkgb=KOR')
    store = BS(driver.page_source, 'html.parser')
    print(KB(store))
elif shop == '2':
    select_store('영풍문고')
    store = BS(driver.page_source, 'html.parser')
    print(YP(store))
r'''
elif shop == '3':
    select_store('반디앤루니스')
    store = BS(driver.page_source, 'html.parser')
r'''