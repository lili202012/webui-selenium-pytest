from common.base import Base
from common.config import host
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
import time

# host = "http://49.235.92.12:8020"
login_url = host + "/login"

class LoginPage(Base):
    '''登录页面'''

    #named定位，账号和密码框
    loc1 = (By.NAME, "username")
    loc2 = (By.NAME, "password")
    #css定位，登录按钮
    loc3 = (By.CSS_SELECTOR,'#login-form>div.login-wrap>button')

    # 判断页面元素
    loc4 = (By.CSS_SELECTOR, 'body>section>div.main-content>div.wrapper>div>div>h2')

    @allure.step("登录步骤：输入账号")
    def input_user(self, username):
        '''输入账号'''
        self.send(self.loc1, username)

    @allure.step("登录步骤：输入密码")
    def input_psw(self, psw):
        '''输入密码'''
        self.send(self.loc2, psw)

    @allure.step("登录步骤：点登陆按钮")
    def click_button(self):
        self.click(self.loc3)

    @allure.step("登录")
    def login(self, username="libai", psw="opms123456"):
        self.driver.get(login_url)
        self.input_user(username)
        self.input_psw(psw)
        self.click_button()

    @allure.step("判断是否登录成功, 返回bool值")
    def is_login_success(self):
        '''判断是否登录成功, 返回bool值'''
        text = self.get_text(self.loc4)
        print("登录完成后，获取页面文本元素:%s"%text)
        return text == "让项目管理与OA办公更加轻便！"


if __name__ == '__main__':
    driver = webdriver.Chrome()
    web = LoginPage(driver)
    driver.get("http://127.0.0.1:8088/login")
    #登录
    web.login("libai", "opms123456")
    #time.sleep(30)

    # 判断登录是否成功
    result = web.is_login_success()
    print(result)
    # 释放资源, 退出浏览器
    driver.quit()
    assert result




