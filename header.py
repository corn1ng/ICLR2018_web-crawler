# -*- coding:utf8 -*-
# author: Brett


def return_header():
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu '
                      'Chromium/62.0.3202.94 Chrome/62.0.3202.94 Safari/537.36',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache - Control': 'max - age = 0',
        'Connection': 'keep - alive',
        'Upgrade - Insecure - Requests': '1',
        'Host': 'openreview.net',
        'Origin': 'https://openreview.net',
        'Referer': 'http://www.iclr.cc/doku.php?id=ICLR2018:main&redirect=1',
    }
    return headers


def return_contentheader():
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu '
                      'Chromium/62.0.3202.94 Chrome/62.0.3202.94 Safari/537.36',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep - alive',
        'Host': 'openreview.net',
    }
    return headers

