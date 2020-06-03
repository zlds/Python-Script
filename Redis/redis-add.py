# -*- coding: utf-8 -*-
import redis


# 添加key到redis
def add(key_name):
    # redis连接
    rs = redis.StrictRedis(host='localhost', port=6379, db=0)  # db默认为0
    for i in range(1, 501):
        rs.set(key_name + str(i), str(i))
    rs.close()


add('user')
