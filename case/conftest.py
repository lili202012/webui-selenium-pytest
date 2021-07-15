
#Windows执行
# from selenium import webdriver
# import time
# import pytest
# from pages.login_page import LoginPage
#
# @pytest.fixture(scope="session")
# def driver(request):
#     '''定义全局driver'''
#     _driver = webdriver.Chrome()
#     # 最大化窗口
#     _driver.maximize_window()
#
#     def end():
#         '''测试用例完成后，执行终结函数'''
#         #等待时间
#         time.sleep(60)
#         #释放资源, 退出浏览器
#         _driver.quit()
#
#     #终结函数，就是后置，用例执行完后再执行end函数
#     #request是pytest中的内置fixture
#     request.addfinalizer(end)
#     return _driver
#
#
# @pytest.fixture(scope="session")
# def login(driver):
#     '''前置：登录'''
#     web = LoginPage(driver)
#     web.login()
#     return driver


#Linux执行
# from pages.login_page import LoginPage
# from selenium import webdriver
# import pytest
# import time
# from selenium.webdriver.chrome.options import Options
#
# # 命令行参数,注册自定义参数headless
# def pytest_addoption(parser):
#     ''''添加命令行参数'''
#     parser.addoption(
#         '--headless', action="store",
#         default='no', help='set chrome headless option yes or no'
#     )
#
# @pytest.fixture(scope="session")
# def driver(request):
#     """定义全局driver fixture，给其它地方作参数调用"""
#     headless = request.config.getoption("--headless")
#     chrome_options = Options()
#     chrome_options.add_argument('--window-size=1920,1080')  # 设置当前窗口的宽度和高度
#     if headless=="yes":
#         chrome_options.add_argument('--headless')  # 无界面
#
#     _driver = webdriver.Chrome(chrome_options=chrome_options)
#     # _driver = webdriver.Chrome()
#     # 窗口最大化
#     # _driver.maximize_window()
#     def end():
#         print("全部用例执行完后 teardown quit dirver")
#         time.sleep(5)
#         _driver.quit()
#     request.addfinalizer(end)
#     return _driver
#
# @pytest.fixture(scope="session")
# def login(driver):
#     web = LoginPage(driver)
#     web.login()
#     return driver



#判断是window还是Linux
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def is_windows_linux():
    '''判断当前系统是windows还是linux:
    一般linux结果为('32bit','ELF')ELF或者('64bit','ELF')ELF，
    windows为('32bit','windowsPE')或者('64bit','windowsPE')'''
    chrome_options = Options()
    # 设置当前窗口的宽度和高度
    chrome_options.add_argument('--window-size=1920,1080')

    # 可以先判断是否启动无界面
    chrome_options.add_argument('--headless') # 无界面

    #输出当前设备信息
    print(sys.platform)
    #若是window，则使用有界面的操作；Linux则使用无界面的操作
    if "win"  in sys.platform:
        print("当前运行的操作系统是windows,请确认是操作系统是否判断正确")
        driver = webdriver.Chrome()
    else:
        print("当前运行的操作系统是linux,请确认是操作系统是否判断正确")
        # 解决DevToolsActivePort文件不存在报错问题
        chrome_options.add_argument('--no-sandbox')
        # 禁用GPU硬件加速。如果软件渲染器没有就位，则GPU进程将不会启动。
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(options=chrome_options)
    return driver

driver = is_windows_linux()
driver.get("https://www.baidu.com")

















