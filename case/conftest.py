from selenium import webdriver
import time
import pytest
from pages.login_page import LoginPage

@pytest.fixture(scope="session")
def driver(request):
    '''定义全局driver'''
    _driver = webdriver.Chrome()
    # 最大化窗口
    _driver.maximize_window()

    def end():
        '''测试用例完成后，执行终结函数'''
        #等待时间
        time.sleep(60)
        #释放资源, 退出浏览器
        _driver.quit()

    #终结函数，就是后置，用例执行完后再执行end函数
    #request是pytest中的内置fixture
    request.addfinalizer(end)
    return _driver


@pytest.fixture(scope="session")
def login(driver):
    '''前置：登录'''
    web = LoginPage(driver)
    web.login()
    return driver


