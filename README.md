# JHU(Join Happy Utils)
> 这个是我自己编写的一个python工具库,简化或者自动化的帮助我做一些工作

# ChangeLog
## 2023-10-23
### ==更新==webdriver
- 更新了默认chrome驱动的下载版本为88.0.4324.27,当浏览器版本低于该版本内的时候,可能无法正常运行使用

## 2023-10-17
### ==更新==webdriver
- 追加了在windows环境下,驱动名为chromedirver.exe的设定,同时下载完成后移除不必要的文件,仅保留驱动文件


## 2023-10-08
### ==新增==WebHook
- 支持发送dingding的webhook,支持text类型和link类型的快速构建和发送

## 2023-09-14
### ==更新==webdriver
- 从浏览器版本115开始,使用新的地址下载链接,请确保你的网络能够访问该地址 https://googlechromelabs.github.io/chrome-for-testing/

## 2023-03-06
### ==新增==钉钉扫码登录
- 支持生成钉钉扫码登录的url
- 支撑获取钉钉扫码登录的用户信息

## 2022-11-17
### ==新增==Python3.11支持
- 2022-11-17起,工具基于python3.11版本进行开发

## 2022-11-10
### ==新增==webdirver
- 支持运行chrome自动化脚本
 
## 2022-07-01
### ==新增==email模块
- 支持SMTP发送邮件

## 2022-06-09
### ==新增==webhook模块
- 企业微信发送webhook消息,当前仅支持text格式
