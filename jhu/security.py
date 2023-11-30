"""
安全模块工具
"""
from datetime import datetime,timedelta
from bcrypt import checkpw,gensalt,hashpw
from base64 import b64decode
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import unpad
from jose import jwt

class HashAPI:
    def __init__(self,key:str) -> None:
       self.__key = key

    @property
    def key(self):
       return self.__key
    
    def hash_text(self,plain_text:str)->str:
        return hashpw(plain_text.encode(),gensalt()).decode()

    def decrypt(self,hash_text:str)->str:
        cipher = AES.new(self.key.encode(),AES.MODE_ECB)
        enc_text = b64decode(hash_text)
        dec_text = unpad(cipher.decrypt(enc_text),AES.block_size).decode()
        return dec_text

    def verifty(self,plain_text:str,hash_text:str)->bool:
        return checkpw(plain_text.encode(),hash_text.encode())


class JWTAPI:
    def __init__(self,key:str,expire_min:int,algorithm:str='HS256') -> None:
        self.__key = key
        self.__algorithm = algorithm
        self.expire = expire_min

    @property
    def key(self):
        return self.__key
    
    @property
    def algorithm(self):
        return self.__algorithm
    
    def encode(self,**kw)-> str:
        expire = datetime.utcnow() + timedelta(minutes=self.expire)
        payload = dict(**kw,exp=expire)
        return jwt.encode(payload,key=self.key,algorithm=self.algorithm)

    def decode(self,token:str)->dict:
        return jwt.decode(token=token,key=self.key,algorithms=self.algorithm)