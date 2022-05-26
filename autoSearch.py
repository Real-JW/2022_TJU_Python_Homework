#-*-coding=utf-8

import requests
from bs4 import BeautifulSoup

# url = "http://www.tju.edu.cn"
url = "http://www.baidu.com"

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status() #如果状态不是200，引发异常
        r.encoding = 'utf-8' #无论原来用什么编码，都改成utf-8
        return r.text
    except:
        return ""

def getLinks(url):
    html = getHTMLText(url)
    #创建一个BeautifulSoup解析对象
    soup = BeautifulSoup(html, "html.parser")
    #获取所有的链接
    links = soup.find_all('a')
    return links

# def autoSearch():
#     # print(getHTMLText(url))
#     file = open('link.txt','w')
#     links = getLinks(url)
#     print ("所有的链接")
#     for link in links:
#         link.encoding = 'utf-8'
#         # print (link['href'], link.get_text())
#         strLink = link['href']+link.get_text()
#         file.write(strLink+"\n")
#         links2 = getLinks(link['href'])
#         print ( "Second Page" )
#         for link2 in links2:
#             str2 = link2.a['href']+link2.get_text()
#             file.write("\t"+str2+"\n")
#             # print ('  ', link2['href'], link2.get_text())
#     return 0

def autoSearch():
    # print(getHTMLText(url))
    links = getLinks(url)
    print ("所有的链接")
    for link in links:
        print (link['href'], link.get_text())
        links2 = getLinks(link['href'])
        print ( "Second Page" )
        for link2 in links2:
            print ('  ', link2['href'], link2.get_text())
    return 0

if __name__ == '__main__':
    autoSearch()

