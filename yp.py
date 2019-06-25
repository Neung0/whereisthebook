from selenium import webdriver
from bs4 import BeautifulSoup

def chk_stock(soup):
    stock = {}
    store = soup.select('.tb_store strong')
    num = soup.select('.tb_store span')
    for i, j in zip(store, num):
        stock[i.text] = j.text
    return stock

if __name__=='__main__':
    driver = webdriver.Chrome(r'C:\Users\smddu\Documents\chromedriver\chromedriver.exe')
    driver.get('http://www.ypbooks.co.kr/book.yp?bookcd=100860837&gubun=NV')
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    a = chk_stock(soup)
    print(a)
