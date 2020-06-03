# -*- coding: utf-8 -*-
import redis


def get_key(key_name):
    # 创建连接池
    pool = redis.ConnectionPool(host='localhost', port=6379, db=0)

    # 建立连接对象  (注意、只有使用到才会和redis建立连接)
    rs = redis.Redis(connection_pool=pool)

    # 查看key
    result = rs.get(key_name)
    print(result)


get_key('user1')
