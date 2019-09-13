from urllib.request import urlopen
from bs4 import BeautifulSoup

#=======================================


html = urlopen("https://python.org/about")
bsObject = BeautifulSoup(html, "html.parser")
naver = urlopen("https://naver.com")
NaverCon = BeautifulSoup(naver, "html.parser")

print (bsObject.head.find("meta",{"name" : "description"}).get('content'))
print (NaverCon.head.find("meta",{"name" : "description"}).get('content'))

for link in bsObject.find_all('a'):
    print (link.text.strip(), link.get('href'))

print ("\n\n\n")

for link in NaverCon.find_all('a'):
    print (link.text.strip(), link.get('href'))
