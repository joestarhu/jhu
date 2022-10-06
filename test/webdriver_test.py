from jhu.webdriver import WebdriveChrome

if __name__ == '__main__':
    web = WebdriveChrome()
    web.driver.get('https://www.zjzwfw.gov.cn/zjservice/front/index/page.do?webId=1')
