# -*- coding:utf8 -*-
# author: Brett
import requests


def parsejson(URL, headers):
    jsons = requests.get(URL, headers=headers)
    answer = jsons.json()
    ids = []
    for i in answer['notes']:
        ids.append(i['id'])
    return ids