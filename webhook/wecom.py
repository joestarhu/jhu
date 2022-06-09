"""
作者:J.Hu
日期:2022-06-09
内容:
- 企业微信发送webhook消息,当前仅支持text格式
"""
from enum import Enum
from typing import Optional
from requests import Session

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
        if len(content) >= 2048:
            raise Exception('content内容长度不能超过2048字节')
        super().__init__(msgtype=WeComMsgType.txt.value, content=content,
                         mentioned_list=mentioned_list, mentioned_mobile_list=mentioned_mobile_list)
class WeComHook:
    def __init__(self, url: str):
        self.url = url

    def send(self, content: Optional[TextContent]):
        s = Session()
        rsp = s.post(self.url, json=content.data)
        rsp.encoding = rsp.apparent_encoding
        return rsp

if __name__ == '__main__':
    """
    wh = WeComHook('https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=61afd9ee-47d8-4be2-b7d0-49e535abf2db')
    t = WeComText("大家好,请大家在本日17:00之前,将周报发送给胡健;周报文件名统一为：产品设计2部-XXX-工作周报(YYYYMMDD-YYYYMMDD)比如： 产品设计2部-胡健-工作周报(20210628-20210702）,同时周报里面的本周日期和下周日期也要检查下", ['@all'])
    wh.send(t)
    """
