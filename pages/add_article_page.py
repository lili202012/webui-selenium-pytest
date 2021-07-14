from common.base import Base
import allure
from selenium import webdriver
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class ArticleclassifyPage(Base):

    xiangmu = (By.XPATH,'//span[contains(text(),"项目管理")]')
    add_xiangmu = (By.XPATH,'//a[@class="btn btn-success"]')
    add_name = (By.XPATH,'//input[@placeholder="请填写名称"]')
    add_aliasname = (By.XPATH,'//input[@placeholder="取个代号"]')
    add_miaoshu = (By.XPATH,'//*[@id="project-form"]/div[4]/div/div/div[2]/iframe')
    tijiao = (By.XPATH,'//button[@class="btn btn-primary"]')
    close = (By.XPATH,'//*[@id="projectModal"]/div/div/div[1]/button')

    aa = (By.XPATH,'//table')


    @allure.step("打开项目管理页面")
    def click_xiangmu(self):
        self.click(self.xiangmu)

    @allure.step("添加新项目")
    def add_new_xiangmu(self,name="我是名称6",aliasname="我是别名",miaoshu="我是描述"):
        #点击添加新项目
        self.click(self.add_xiangmu)
        self.send(self.add_name,name)
        self.send(self.add_aliasname,aliasname)
        self.send(self.add_miaoshu,miaoshu)
        self.click(self.tijiao)
        time.sleep(1)
        #self.click(self.close)
        self.js_click(self.close)


    @allure.step("验证项目是否添加成功，成功返回true，失败是false")
    def is_add_xiangmu_success(self,test="我是名称2"):
        self.click(self.xiangmu)
        table = self.get_text(self.aa)
        #print(table)
        return test in table


if __name__ == '__main__':
    driver = webdriver.Chrome()
    # 最大化
    driver.maximize_window()
    web = LoginPage(driver)
    web.login()
    res = web.is_login_success()
    print("登录结果：%s"%res)

    #添加项目
    edit = ArticleclassifyPage(driver)
    edit.click_xiangmu()
    edit.add_new_xiangmu()
    res = edit.is_add_xiangmu_success()
    print("新项目是否添加成功：%s"%res)

