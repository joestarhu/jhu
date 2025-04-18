# JHU(Join Happy Utils)
> 这个是我自己编写的一个python工具库,简化或者自动化的帮助我做一些工作

# ChangeLog
## V1.6.6(2025-03-27)
### orm.py
- counts函数修复

## V1.6.5(2025-03-27)
### orm.py
- pagination函数total为零的时候,不继续执行SQL,直接返回空的结果

## V1.6.4(2024-12-31)
### orm.py
- 修复了counts函数:select语句中如果带有group by字段,那么with_only_columns会导致总数计算不正确

## V1.6.3(2024-11-22)
### security.py
- AESAPI追加了手机号的加密和解密方法

## V1.6.0(2024-08-08)
### orm.py
- 追加了pytz,created_at和updated_at均是utc的时间来展示内容.默认Asia/Shanghai.

## V1.5.2(2024-06-21)
### orm.py
- 追加了check
- 优化all和one

## V1.5.1(2024-06-19)
### orm.py
- 文件重命名

## V1.5.0(2024-04-16)
### data.py
- 新增orm模块

### auth.py
- 修改了参数名字,DINGDING->DINGTALK

## V1.4.2(2024-04-12)
### security.py
- 整合了HashAPI和AESAPI的解密功能

## V1.4.1(2024-04-10)
### security.py
- 废弃fernetAPI,改为AESAPI,并采用ECB模式; 同样的明文加密后的内容是一致的

## V1.4.0(2024-04-09)
### security.py
- 追加了对称加密
- JWTAPI中的datetime.utcnow函数弃用,用了其他替代方法

## 更早的版本说明(history)
- 2023-12-19:从v1.3.0版本开始,基于python3.12进行开发.并整合优化代码
- 2023-11-30:DrissionPage具备了更强的能力,selenium不在使用,因此移除掉webdriver,追加了jwt和hash password的能力
- 2023-10-24:更新了auth,移除了钉钉,整合了钉钉和飞书的三方扫码登录
- 2023-10-23:更新了默认chrome驱动的下载版本为88.0.4324.27,当浏览器版本低于该版本内的时候,可能无法正常运行使用
- 2023-10-17:追加了在windows环境下,驱动名为chromedirver.exe的设定,同时下载完成后移除不必要的文件,仅保留驱动文件
- 2023-10-08:支持发送dingding的webhook,支持text类型和link类型的快速构建和发送
- 2023-09-14:从浏览器版本115开始,使用新的地址下载链接,请确保你的网络能够访问该地址 https://googlechromelabs.github.io/chrome-for-testing
- 2023-03-06:支持生成钉钉扫码登录的url,支撑获取钉钉扫码登录的用户信息
- 2022-11-17:工具基于python3.11版本进行开发
- 2022-11-10:支持运行chrome自动化脚本
- 2022-07-01:支持SMTP发送邮件
- 2022-06-09:企业微信发送webhook消息,当前仅支持text格式
