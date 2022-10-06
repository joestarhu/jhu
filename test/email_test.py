#!/usr/bin/env python3
import sys
sys.path.append('/Users/hujian/code/jhu')


from jhu.email import Mail




if __name__ == '__main__':
    # server = 'smtp.qq.com'
    server = 'smtp.qiye.aliyun.com'
    user = 'hujian@morewin.tech'
    # pwd = 'izzzrdislhwpbied'
    pwd = 'Morewin1@'
    m = Mail(server)
    m.login(user, pwd, 'hello_world')

    attach = ['/Users/hujian/code/jhu/requirements.txt']

    m.add_receiver_to('joestarhu@163.com', 'to_name')
    m.add_receiver_cc('joestarhu@163.com', 'cc_name')
    m.add_receiver_bcc('joestarhu@163.com')
    m.send('这是一次测试', '请注意这是一次测试演戏', attach)
