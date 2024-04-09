#!/usr/bin/env python3
"""
测试
"""

from cryptography.fernet import Fernet
from jhu.security import HashAPI,JWTAPI,FernetAPI

if __name__ == '__main__':
    KEY = '12345678'
    api_hash = HashAPI(KEY)

    print(api_hash.verifty('qwe321',api_hash.hash_text('qwe321')))

    api_jwt = JWTAPI(KEY,1)
    print(api_jwt.decode(api_jwt.encode(a=1)))
    api_fernet = FernetAPI(Fernet.generate_key())    
    print(api_fernet.decrypt(api_fernet.encrypt('qwe321')))

