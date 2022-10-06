[toc]

# 示范操作
```python
# 引入Email模块
from jhu.email import Mail


host = 'smtp.jhu.test.com'  # 设定SMTP服务器地址
user = 'username' # 设置smtp服务器登录名
pwd = 'pwd' # 设置密码


# 实例化Mail对象
m = Mail(host)

# 使用账户密码登录,可以选填nickname,nickname就是发送邮件时的姓名,不填写默认是使用发件人邮箱地址
obj.login(user,pwd,nickname='J.Hu')

# 设置to的接收对象,如果需要发送给多人,则需要多次调用
m.add_receiver_to('to_name@jhu.com', 'to_name')
m.add_receiver_to('to_name_1@jhu.com', 'to_name')

# 设置cc的接收对象
m.add_receiver_cc('cc_name@jhu.com', 'cc_name')

# 设置bcc的接收对象
m.add_receiver_bcc('bcc_name@jhu.com')

# 清空to,cc,bcc的内容
m.clear_receiver_lst()

# 查看to,cc,bcc的列表对象
m.receive_to()
m.receive_cc()
m.receive_bcc()


#附件要以List的形式传入,可以发送多个附件...
attach = ['/jhu/requirements.txt']

# 发送邮件,可设置标题,内容,和附件
m.send(title='这是一次测试', content='请注意这是一次测试演戏') # 发送不带附件
m.send(title='这是一次测试', content='请注意这是一次测试演戏', attach_lst=attach) # 发送带附件


# 最后使用完成后,关闭连接
m.disconnect()
```
