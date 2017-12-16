# -*- coding:utf8 -*-
# author: Brett
import redis


def redis_conn():
    pool = redis.ConnectionPool(host='localhost', port=6379,
                                decode_responses=True)
    r = redis.Redis(connection_pool=pool)
    return r


def save_to_redis(title, score, conn):
    conn.hset(name='iclrscore', key=title, value=score)
