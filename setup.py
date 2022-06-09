#! /usr/bin/env python3

"""
制作PIP包教程
1. 先设置一个setup文件
"""
from distutils.core import setup
import setuptools

setup(
    name='jhu',  # 包的名称
    version='1.0.0',  # 包的版本,每次更新或升级包都需要更新它
    description='jhu是一个个人工具包,简化或自动化的做一些任务', #包的描述
    author='J.Hu',  # 作者
    email='joestarhu@163.com', # 作者邮箱
    url='https://github.com/joestarhu/jhu', # 项目地址
    packages=setuptools.find_packages(
        exclude=['test', 'examples', 'script', 'tutorials']),   # 包内不需要引用的文件
    classifiers=[
            "Environment :: Web Environment",
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Operating System :: MacOS',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Programming Language :: Python :: 3.8',
    ],
    install_requires=['requests','pydantic'], # 依赖的包
    zip_safe = True
)
