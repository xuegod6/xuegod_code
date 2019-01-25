from selenium import webdriver
import time
from fake_useragent import UserAgent
import sys
opt = webdriver.ChromeOptions()
# opt.add_argument('--headless')
#更换头部
ua = UserAgent()
opt.add_argument('user-agent="%s"' % ua.random)
driver = webdriver.Chrome(chrome_options=opt)
class HongZha:
    def __init__(self):
        self.phone = sys.argv[1:]
        self.num = 0
    # 发送验证码
    def send_yzm(self,button,name):
        button.click()
        self.num+=1
        print("{}  第{}次  发送成功  {}".format(self.phone,self.num,name))

    # qq注册接口
    def qq(self,name):
        driver.get('https://ssl.zc.qq.com/v3/index-chs.html')
        driver.implicitly_wait(10)
        driver.find_element_by_xpath('//input[@id="nickname"]').send_keys('xxxx')
        driver.find_element_by_xpath('//input[@id="password"]').send_keys('woshinibaba22')
        driver.find_element_by_xpath('//input[@id="phone"]').send_keys(self.phone)
        button = driver.find_element_by_xpath('//a[@id="send-sms"]')
        self.send_yzm(button,name)

    # 小米注册接口
    def xiaomi(self,name):
        driver.get('https://account.xiaomi.com/pass/register')
        driver.implicitly_wait(10)
        driver.find_element_by_xpath('//input[@name="phone"]').send_keys(self.phone)
        button = driver.find_element_by_xpath('//input[@type="submit"]')
        self.send_yzm(button,name)
    # 瓜子注册接口
    def guazi(self,name):
        driver.implicitly_wait(10)
        driver.get ( "https://www.guazi.com/www/bj/buy" )
        a_btn = driver.find_element_by_xpath ( "//a[@class='uc-my']" )
        a_btn.click ()
        tel = driver.find_element_by_xpath ( "//input[@placeholder='请输入您的手机号码']" )
        tel.send_keys ( self.phone )
        button = driver.find_element_by_xpath ( "//button[@class='get-code']" )
        self.send_yzm ( button,name )

    # 唯品会注册接口
    def wphui(self,name):
        driver.get ( "https://passport.vip.com/register?src=https%3A%2F%2Fwww.vip.com%2F" )
        driver.implicitly_wait(10)
        tel = driver.find_element_by_xpath ( "//input[@placeholder='请输入手机号码']" )
        tel.send_keys ( self.phone )
        driver.find_element_by_xpath ( '//a[contains(./text(),"获取验证码")]' ).click()
        button = driver.find_element_by_xpath ("//a[@class='ui-btn-medium btn-verify-code ui-btn-secondary']" )
        self.send_yzm ( button,name )
    # 苏宁注册接口
    def suning(self,name):
        driver.get ( "https://reg.suning.com/person.do" )
        driver.implicitly_wait(10)
        tel = driver.find_element_by_xpath ( "//input[@id='mobileAlias']" )
        tel.send_keys ( self.phone )
        button = driver.find_element_by_xpath ("//a[@id='sendSmsCode']" )
        self.send_yzm ( button,name )
    #一号店注册接口
    def yhd(self,name):
        driver.get ( "https://passport.yhd.com/passport/register_input.do" )
        driver.implicitly_wait(10)
        a = driver.find_element_by_class_name('agree-btn')
        a.click()
        driver.find_element_by_xpath ( "//input[@id='userName']" ).send_keys("wujunya625")
        tel = driver.find_element_by_xpath ( "//input[@id='phone']" )
        tel.send_keys ( self.phone )
        button = driver.find_element_by_xpath ("//a[contains(./text(),'获取验证码')]" )
        self.send_yzm ( button,name )
    # 有赞注册接口
    def youzan(self,name):
        driver.get('https://www.youzan.com/v2/account?from_source=baidu_pz_shouye_0&')
        driver.implicitly_wait(10)
        driver.find_element_by_xpath('//input[@name="mobile"]').send_keys(self.phone)
        button = driver.find_element_by_xpath('//button[contains(./text(),"获取验证码")]')
        self.send_yzm(button, name)
    # 拼多多短信登陆接口
    def pinduoduo(self,name):
        driver.get('http://mobile.yangkeduo.com/login.html')
        driver.implicitly_wait(10)
        driver.find_element_by_xpath('//div[@class="phone-login"]/span').click()
        driver.find_element_by_xpath('//input[@id="user-mobile"]').send_keys(self.phone)
        button=driver.find_element_by_xpath('//button[@id="code-button"]')
        self.send_yzm(button, name)
    # 大众点评登陆接口
    def dianping(self,name):
        driver.get('https://maccount.dianping.com/login')
        driver.implicitly_wait(10)
        driver.find_element_by_xpath('//input[@name="mobile"]').send_keys(self.phone)
        button = driver.find_element_by_xpath('//a[@class="J_send EasyLogin_send"]')
        self.send_yzm(button, name)
    # 循环执行
    def main(self):
        while True:
            self.xiaomi('小米')
            self.guazi('瓜子')
            self.wphui('唯品会')
            self.youzan('有赞')
            self.pinduoduo('拼多多')
            self.dianping('大众点评')
            time.sleep(5)
if __name__ == '__main__':
    hongzha = HongZha()
    hongzha.main()