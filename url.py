# -*- coding:utf8 -*-
# author: Brett


def geturl():
    urllist = []
    for i in range(0, 1050, 50):
        URL = 'https://openreview.net/notes?invitation=ICLR.cc%2F2018%2FConference%2F-%2FBlind_Submission&offset=' + str(
            i) + '&limit=50'
        urllist.append(URL)
    return urllist


def get_specify_content_url(conn):
    all_paper = conn.hgetall('iclr')
    urllist = []
    for i in all_paper:
        m = {}
        m = conn.hget('iclr', i)
        id = (eval(m)['id'])
        urllist.append('https://openreview.net/notes?forum=' + str(id) + '&trash=true')
    return urllist