# -*- coding:utf8 -*-

import urllib.request
from bs4 import BeautifulSoup


def html_parse(url):
    html = urllib.request.urlopen(url)
    content = BeautifulSoup(html, 'html.parser')
    return content


def html_search(html, search_content):
    list = html.findAll(search_content)
    return list[0].get_text()

if __name__ == '__main__':
    content = html_parse("http://www.sogou.com")
    print(html_search(content, {'h1','div','body'}))
