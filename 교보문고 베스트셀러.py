from urllib.request import urlopen
from bs4 import BeautifulSoup
#===================================

html = urlopen("https://www.kyobobook.co.kr/bestSellerNew/bestseller.laf")
Best = BeautifulSoup(html,"html.parser")
##교보문고 베스트셀러 웹페이지 가져오기




book_page_urls=[] # 해당 페이지 URL리스트화?
for cover in Best.find_all('div', {'class':'detail'}):  #div항목 및 class가 "detail"인거 추출?
    link = cover.select('a')[0].get('href') #
    book_page_urls.append(link)
## 책의 상세 웹페이지 주소를 추출하여 리스트에 저장

for index, book_page_url in enumerate(book_page_urls): #book_page_urls수 만큼 for문 돌리기?
    html = urlopen(book_page_url)
    Best = BeautifulSoup(html, "html.parser")
    title = Best.find('meta', {'property':'rb:itemName'}).get('content')
    author = Best.select('span.name a')[0].text
    image = Best.find('meta',{'property':'rb:itemImage'}).get('content')
    url = Best.find('meta',{'property':'rb:itemUrl'}).get('content')
    originalPrice = Best.find('meta',{'property':'rb:originalPrice'}).get('content')
    salePrice = Best.find('meta',{'property':'rb:salePrice'}).get('content')
##메타정보로부터, 필요한 정보들 추출.


    print(index+1, title, author, image, url, originalPrice, salePrice)
                          
    
    




