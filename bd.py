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
    driver.get('http://www.bandinlunis.com/front/product/detailProduct.do?prodId=3483882')
    print(driver.page_source)
    #soup = BeautifulSoup(driver.page_source, 'html.parser')
    #print(soup)
    """
    store = soup.select('div.mt30 th')
    num = soup.select('div.mt30 td > a')
    print(store)
    print(num)
    """