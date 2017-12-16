# -*- coding:utf8 -*-
# author: Brett
from header import return_header
from header import return_contentheader
from redis_coon import redis_conn
from url import geturl
from iclr import parsejson
from url import get_specify_content_url
from iclr import parse_specify_content
from redis_coon import save_to_redis

if __name__ == '__main__':
    head = return_header()
    # UR = 'https://openreview.net/notes?invitation=ICLR.cc%2F2018%2FConference%2F-%2FBlind_Submission&offset=0&limit=50'
    conn = redis_conn()
    urllist = geturl()
    for i in urllist:
        parsejson(i, headers=head, conn=conn)
    xinlist = get_specify_content_url(conn)
    # print((xinlist))
    # CONTENT_URL = 'https://openreview.net/notes?forum=SyBPtQfAZ&trash=true'

    contentheader = return_contentheader()
    # parse_content(CONTENT_URL, contentheader)

    for i in xinlist:
        title, socre = parse_specify_content(i, contentheader)
        save_to_redis(title, socre, conn)
