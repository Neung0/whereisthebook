# 오디오북이 있는 책은 응답코드가 500
# 즉, 서버단에서 크롤링을 차단하는 것으로 보임
# 어쩔 수 없이 셀레니움 쓰기로..

import re
import requests
from urllib import parse
from bs4 import BeautifulSoup as BS

headers = {'Content-Type': 'application/xml'}
audio = 'https://book.naver.com/bookdb/book_detail.nhn?bid=14300423'
url = 'https://book.naver.com/bookdb/book_detail.nhn?bid=14841090'
req = requests.get(audio, headers=headers)
print(req, req.text)