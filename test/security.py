"""
测试
"""

from jhu.security import HashAPI,JWTAPI

KEY = '12345678'
api_hash = HashAPI(KEY)

api_hash.verifty('qwe321',api_hash.hash_text('qwe321'))

api_jwt = JWTAPI(KEY,1)
api_jwt.encode(a=1)
api_jwt.decode(api_jwt.encode(a=1))