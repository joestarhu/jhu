"""
日期:2023-12-01
内容:
- 集成钉钉和企业微信的webhook能力
参考文档:
- https://open.dingtalk.com/document/robots/custom-robot-access
- https://developer.work.weixin.qq.com/document/path/91770
"""
from base64 import b64encode
from enum import Enum
from hashlib import sha256
from hmac import new as hmac_new
from requests import session
from time import time
from urllib.parse import quote_plus


class BaseHook:
    def __init__(self,url:str,sk:str = None) -> None:
        """
        url:webhook的url地址
        sk:加签密钥
        """
        self.__url = url
        self.sk = sk

    @property
    def url(self):
        return self.__url


    def send(self,data,url):
        with session() as s:
            s.post(url,json=data)



class WeComMsgType(str, Enum):
    txt = 'text'


class BaseContent:
    def __init__(self, **kw):
        self._data = kw

    @property
    def data(self) -> dict:
        return self._data

    @data.setter
    def data(self, data):
        self._data = data


class WeComText(BaseContent):
    def __init__(self, content: str, mentioned_list: Optional[list] = None, mentioned_mobile_list: Optional[list] = None):
        if len(content) > 2048:
            raise Exception('content内容长度不能超过2048字节')
        super().__init__(msgtype=WeComMsgType.txt.value, content=content,
                         mentioned_list=mentioned_list, mentioned_mobile_list=mentioned_mobile_list)


class WeComHook:
    def __init__(self, url: str):
        self.url = url

    def send(self, content: Optional[WeComText]):
        s = Session()
        rsp = s.post(self.url, json=content.data)
        rsp.encoding = rsp.apparent_encoding
        return rsp


if __name__ == '__main__':
    wh = WeComHook('******')
    t = WeComText("大家好,请", ['@all'])
    wh.send(t)
