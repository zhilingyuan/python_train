import requests
from bs4 import BeautifulSoup
import bs4
r=requests.get('http://python123.io/ws/demo.html')
demo=r.text
soup=BeautifulSoup(demo,'html.parser')
print(soup.prettify(),'\n')
print(soup.a.name,'\n',
soup.a.parent.name,'\n',
soup.a.parent.parent.name,'\n')
tag=soup.a
print(tag.attrs,'\n',
      type(tag),'\n',
      type(tag.attrs))
print('\n',soup.a,soup.a.string,'\n',type(soup.p.string))
for link in soup.find_all('a'):
    print(link.get('href'))

#def getHTMLText(url):
    
