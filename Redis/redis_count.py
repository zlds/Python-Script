# -*- coding: utf-8 -*-
import redis


# 连接redis 实例
rserver = redis.ConnectionPool(host='localhost', port=6379)

# 统计redis中key的数量
def count():
    r = redis.Redis(connection_pool=rserver)
    result = r.dbsize()
    print('db1中的数量: ', result)

count()