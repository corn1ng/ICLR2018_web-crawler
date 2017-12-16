# -*- coding:utf8 -*-
# author: Brett

import requests
import json
import time


def parsejson(URL, headers, conn):
    jsons = requests.get(URL, headers=headers)
    answer = jsons.json()
    for i in answer['notes']:
        # print(i['content']['title']+'   '+i['id'])
        val ={'replyCount': i['replyCount'],
              'id': i['id'],
              'keywords': i['content']['keywords'],
              }
        conn.hset(name='iclr', key=i['content']['title'], value=val)


def parse_specify_content(URL, headers):
    jsons = requests.get(URL,headers)
    answer = jsons.json()
    score = 0
    index = 0
    for i in answer['notes']:
        try:
            score = score + int(str(i['content']['rating']).split(':')[0])
            index = index+1
        except KeyError:
            pass
    try:
        avgscore = score/index
    except ZeroDivisionError:
        avgscore = 0
    avg_score = ('%.2f' % avgscore)
    title = answer['notes'][0]['forumContent']['title']
    return title, avg_score


if __name__=='__main__':
    print("iclr")