# coding=utf-8

import urllib2
import urlparse
import random
import time
import re
from bs4 import BeautifulSoup
from lxml import etree


url = 'http://www.biquzi.com/4_4965/'
url = 'http://www.biquzi.com/4_4962/'

def set_header():
    headers=[
        {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'},
        {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0'},
        {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'},
    ]

    return headers[random.randrange(0, len(headers))]

def html_download(url):
    req = urllib2.Request(url=url, headers=set_header())
    return urllib2.urlopen(req).read().decode('gbk')

def html_parser(html):
    # html = html.decode('gbk').encode('utf-8')
    s_time = time.time()
    soup = BeautifulSoup(html, 'lxml', from_encoding='utf-8')
    name = soup.find('meta', attrs={'property': 'og:title'}).get('content')
    author = soup.find('meta', attrs={'property': 'og:novel:author'}).get('content')
    category = soup.find('meta', attrs={'property': 'og:novel:category'}).get('content')
    intro = soup.find(id='intro').get_text(strip=True)
    last_update = soup.find(id='info').find_all('p')[2].string
    last_update = re.sub(r'最后更新：', '', last_update.encode('utf-8'))

    chapters = soup.find(id='list').find_all('a')
    chapters = map(lambda tag: [urlparse.urljoin(url, tag['href']), tag.string], chapters)

    urls = soup.find(class_='footer_link').find_all('a')
    urls = map(lambda tag: urlparse.urljoin(url, tag['href']), urls)

    e_time = time.time()

    print e_time - s_time
    return name, author, category, intro, last_update, chapters, urls

def html_parser_xpath(html):

    s_time = time.time()
    html = etree.HTML(html)
    "/html/head/meta[14]"
    name = html.xpath('/html/head/meta[14]/@content')[0].encode('utf-8')
    author = html.xpath('/html/head/meta[13]/@content')[0].encode('utf-8')
    category = html.xpath('/html/head/meta[12]/@content')[0].encode('utf-8')
    intro = html.xpath('//*[@id="intro"]/p/text()')[0].encode('utf-8')
    intro = re.sub(r'^\s*|\s*$', '', intro)
    last_update = html.xpath('//*[@id="info"]/p[3]/text()')[0].encode('utf-8')
    last_update = re.sub(r'最后更新：', '', last_update)

    chapters = html.xpath('//*[@id="list"]/dl/dd/a')
    chapters = map(lambda xml: [urlparse.urljoin(url, xml.attrib['href']), xml.text], chapters)
    
    urls = html.xpath('//*[@id="footer"]/div[1]/a')
    urls = map(lambda xml: urlparse.urljoin(url, xml.attrib['href']), urls)

    e_time = time.time()

    print e_time - s_time

    return name, author, category, intro, last_update, chapters, urls


def save_html(html):
    f = open('test.html', 'w')
    f.write(html)
    f.close()

def test_bs():
    # f = open('test.html', 'r')
    # html = f.read()
    # f.close()

    html = html_download(url)
    print_file(html)

def print_file(html):
    name, author, category, intro, last_update, chapters, urls = html_parser_xpath(html)
    f = open('novel.txt', 'w')

    f.write(name + '\n')
    f.write(author+'\n')
    f.write(category+'\n')
    f.write(intro+'\n')
    for chapter in chapters:
        f.write(chapter[1].encode('utf-8')+'\n')
    f.close()

def main():
    url = 'http://www.biquzi.com/4_4965/'
    
    test_bs()


if __name__ == '__main__':
    main()
