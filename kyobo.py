from selenium import webdriver
from bs4 import BeautifulSoup

def chk_stock(soup):
    stock = {}
    store = soup.select('th')
    num = soup.select('a')
    for i, j in zip(store, num):
        i = i.text
        i = i.strip()
        if i == '':
            pass
        else:
            stock[i] = j.text   
    return stock

if __name__=='__main__':
    driver = webdriver.Chrome(r'C:\Users\smddu\Documents\chromedriver\chromedriver.exe')
    driver.get('http://www.kyobobook.co.kr/prom/2013/general/StoreStockTable.jsp?barcode=9788932916200&ejkgb=KOR')
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    a = chk_stock(soup)
    print(a)