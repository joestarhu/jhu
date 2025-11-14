#!/usr/bin/env python3
"""
测试
"""
from jhu.security import HashAPI, JWTAPI, AESAPI


def test_hashapi():
    a = HashAPI()
    plain_text = "1234567890987654321"
    hash_value = a.hash(plain_text)
    assert a.verify(plain_text, hash_value) == True


def test_jwtapi():
    ...


def test_aesapi():
    ...


if __name__ == '__main__':

    # HashAPI
