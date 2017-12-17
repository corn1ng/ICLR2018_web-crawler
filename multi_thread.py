# -*- coding:utf8 -*-
# author: Brett
import threading
from queue import Queue
from header import return_header
from header import return_contentheader
from redis_coon import redis_conn
from url import geturl
from url import get_specify_content_url
from iclr import parse_specify_content
from redis_coon import save_to_redis
from multi_parse import parsejson


class Product(threading.Thread):
    """
        @:param queue 阻塞队列
        @:param name 线程名字
    """
    def __init__(self, name, queue):
        threading.Thread.__init__(self)
        self.name = name
        self.queue = queue
        return

    def run(self):
        conn = redis_conn()
        head = return_header()
        urllist = geturl()
        idss =[]
        ids =[]
        while True:
            for i in urllist:
                ids = parsejson(i, headers=head)
                for i in ids:
                    print(i)
                    self.queue.put(i)


class Consumer(threading.Thread):
    def __init__(self, name, queue):
        threading.Thread.__init__(self)
        self.name = name
        self.queue = queue
        return

    def run(self):
        header = return_contentheader()
        title = []
        avg_score = []
        while True:
            URL = self.queue.get()
            URL = 'https://openreview.net/notes?forum=' + str(URL) + '&trash=true'
            # print(URL)
            t,s = parse_specify_content(URL, header)
            title.append(t)
            avg_score.append(s)
            print(t,s)



