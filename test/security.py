#!/usr/bin/env python3
"""
测试
"""

from jhu.security import HashAPI,JWTAPI

if __name__ == '__main__':
    KEY = '12345678'
    api_hash = HashAPI(KEY)

    print(api_hash.verifty('qwe321',api_hash.hash_text('qwe321')))

    api_jwt = JWTAPI(KEY,1)
    print(api_jwt.decode(api_jwt.encode(a=1)))
