# coding=utf-8

import urllib2
import random
import time
import re
from bs4 import BeautifulSoup
from lxml import etree


def set_header():
    headers=[
        {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'},
        {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0'},
        {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'},
    ]

    return headers[random.randrange(0, len(headers))]

def html_download(url):
    req = urllib2.Request(url=url, headers=set_header())
    return urllib2.urlopen(req).read()

def html_parser(html):
    # html = html.decode('gbk').encode('utf-8')
    s_time = time.time()
    soup = BeautifulSoup(html, 'lxml', from_encoding='utf-8')
    title = soup.find('meta', attrs={'property': 'og:title'}).get('content')
    e_time = time.time()

    print title, e_time - s_time

def html_parser_xpath(html):
    s_time = time.time()
    html = etree.HTML(html)
    name = html.xpath('/html/head/meta[14]/@content')[0]
    author = html.xpath('/html/head/meta[13]/@content')[0]
    category = html.xpath('/html/head/meta[12]/@content')[0]
    last_update = html.xpath('//*[@id="info"]/p[3]/text()')[0]
    pattern = re.compile(r'最后更新：')
    match = pattern.match(last_update.encode('utf-8'))
    
    e_time = time.time()

    print name, author, category, last_update, e_time - s_time

def save_html(html):
    f = open('test.html', 'w')
    f.write(html)
    f.close()

def test_bs():
    f = open('test.html', 'r')
    html = f.read()
    f.close()
    html_parser(html)
    html_parser_xpath(html)


def main():
    url = 'http://www.biquzi.com/4_4965/'
    
    test_bs()


if __name__ == '__main__':
    main()
