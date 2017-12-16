# -*- coding:utf8 -*-
# author: Brett
from redis_coon import redis_conn


def sort_iclr(conn):
    dict1 = {}
    data = conn.hgetall('iclrscore')
    for k,v in zip(data,data.values()):
        dict1[k] = v
    dict2 = sorted(dict1.items(), key=lambda d: d[1],reverse=True)
    # print(dict2)
    for k,v in dict2:
        print(k,v)
    return


if __name__== "__main__":
    conn = redis_conn()
    sort_iclr(conn)