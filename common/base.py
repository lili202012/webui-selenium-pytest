from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchFrameException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

"""封装selenium基本操作"""

class LocatorTypeError(Exception):
    pass


class ElementNotFound(Exception):
    pass


class Base():
    """基于原生的selenium做二次封装"""

    def __init__(self, driver:webdriver.Chrome, timeout=70, t=0.5):
        self.driver = driver
        self.timeout = timeout
        self.t = t

    #定位元素，显示等待
    def find(self, locator):
        """定位到元素，返回元素对象，没定位到，Timeout异常"""
        if not isinstance(locator, tuple):
            raise LocatorTypeError("参数类型错误，locator必须是元祖类型：loc = ('id','value1')")
        else:
            print("正在定位元素信息：定位方式->%s,value值->%s" % (locator[0], locator[1]))
            try:
                #显示等待，最长等待时间10s，检查间隔时间，每隔0.5秒检查一次操作是否完成；
                #EC.presence_of_element_located(locator)：判断目标元素是否已经成功加载
                # until()方法：直到条件成立返回为真，等待结束。如果超时，抛出TimeoutException，将message传入异常。
                ele = WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_element_located(locator))
            except TimeoutException as msg:
                raise ElementNotFound("定位元素出现超时！！！！"
                                      "先把定位技术学好，别复制粘贴xpath, 请检查定位方式，在浏览器先调试成功，观察页面是否正常打开")
            return ele

    def finds(self, locator):
        '''复数定位，返回elements对象'''
        if not isinstance(locator, tuple):
            raise LocatorTypeError("参数类型错误，locator必须是元祖类型：loc = ('id','value1')")
        else:
            print("正在定位元素信息：定位方式->%s,value值->%s" % (locator[0], locator[1]))
            eles = WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_all_elements_located(locator))
            return eles

    #输入文本
    def send(self, locator, text=''):
        '''发送文本'''
        ele = self.find(locator)
        #判断元素是否展示出来
        if ele.is_displayed():
            #输入文本
            ele.send_keys(text)
        else:
            raise ElementNotVisibleException("元素不可见或者不唯一无法输入，解决办法：定位唯一元素，或先让元素可见，或者用js输入")

    #点击元素
    def click(self, locator):
        '''点击元素'''
        ele = self.find(locator)
        if ele.is_displayed():
            ele.click()
        else:
            raise ElementNotVisibleException("元素不可见或者不唯一无法点击，解决办法：定位唯一元素，或先让元素可见，或者用js点击")

    #清空文本
    def clear(self, locator):
        '''清空输入框文本'''
        ele = self.find(locator)
        ele.clear()

    #判断元素是否被选中
    def is_selected(self, locator):
        """判断元素是否被选中，返回bool值"""
        ele = self.find(locator)
        r = ele.is_selected()
        return r

    def is_element_exist(self, locator):
        try:
            self.find(locator)
            return True
        except:
            return False

    #判断当前页面的title是否完全等于预期的字符串
    def is_title(self, title=''):
        """返回bool值"""
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_is(title))
            return result
        except:
            return False

    #判断当前页面的title是否包含预期的字符串
    def is_title_contains(self, title=''):
        """返回bool值"""
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_contains(title))
            return result
        except:
            return False

    #判断某个元素中的text是否包含预期的字符串
    def is_text_in_element(self, locator, text=''):
        """返回bool值"""
        if not isinstance(locator, tuple):
            raise LocatorTypeError("参数类型错误，locator必须是元祖类型：loc = ('id','value1')")
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element(locator, text))
            return result
        except:
            return False

    #判断某个元素的value属性是否包含预期的字符串
    def is_value_in_element(self, locator, value=''):
        """返回bool值，value为空字符串，返回False"""
        if not isinstance(locator, tuple):
            raise LocatorTypeError("参数类型错误，locator必须是元祖类型：loc = ('id','value1')")
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element_value(locator, value))
            return result
        except:
            return False

    #判断页面上是否存在alert
    def is_alert(self, timeout=3):
        try:
            result = WebDriverWait(self.driver, timeout, self.t).until(EC.alert_is_present())
            return result
        except:
            return False

    #获取页面的title
    def get_title(self):
        """获取title"""
        return self.driver.title

    #获取元素的标签文本：text
    def get_text(self, locator):
        """获取文本"""
        if not isinstance(locator, tuple):
            raise LocatorTypeError("参数类型错误，locator必须是元祖类型：loc = ('id','value1')")
        try:
            t = self.find(locator).text
            return t
        except:
            print("获取text失败，返回''")
            return ""

    #获取元素的属性值
    def get_attribute(self, locator, name):
        """获取属性"""
        if not isinstance(locator, tuple):
            raise LocatorTypeError("参数类型错误，locator必须是元祖类型：loc = ('id','value1')")
        try:
            element = self.find(locator)
            return element.get_attribute(name)
        except:
            print("获取%s属性失败，返回''"%name)
            return ''

    #移动到元素target对象的“顶端”与当前窗口的“顶部”对齐
    def js_focus_element(self, locator):
        """聚焦元素"""
        if not isinstance(locator, tuple):
            raise LocatorTypeError("参数类型错误，locator必须是元祖类型：loc = ('id','value1')")
        target = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    def js_scroll_top(self):
        """滚动到顶部"""
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)

    def js_scroll_end(self, x=0):
        """滚动到底部"""
        js = "window.scrollTo(%s, document.body.scrollHeight)"%x
        self.driver.execute_script(js)

    #下拉框操作：找到element的元素标签，通过index选中下拉框
    def select_by_index(self, locator, index=0):
        """通过索引，index是索引第几个，从0开始，默认第一个"""
        if not isinstance(locator, tuple):
            raise LocatorTypeError("参数类型错误，locator必须是元祖类型：loc = ('id','value1')")
        element = self.find(locator)
        Select(element).select_by_index(index)

    # 下拉框操作：找到element的元素标签，通过value选中下拉框
    def select_by_value(self, locator, value):
        """通过value属性"""
        if not isinstance(locator, tuple):
            raise LocatorTypeError("参数类型错误，locator必须是元祖类型：loc = ('id','value1')")
        element = self.find(locator)
        Select(element).select_by_value(value)

    # 下拉框操作：找到element的元素标签，通过文本选中下拉框
    def select_by_text(self, locator, text):
        """通过文本值定位"""
        element = self.find(locator)
        Select(element).select_by_visible_text(text)

    def switch_iframe(self, id_index_locator):
        """切换iframe"""
        try:
            if isinstance(id_index_locator, int):
                self.driver.switch_to.frame(id_index_locator)
            elif isinstance(id_index_locator, str):
                self.driver.switch_to.frame(id_index_locator)
            elif isinstance(id_index_locator, tuple):
                ele = self.find(id_index_locator)
                self.driver.switch_to.frame(ele)
        except:
            print("iframe切换异常")

    #浏览器切换窗口
    def switch_handle(self, window_name):
        self.driver.switch_to.window(window_name)

    #判断窗口是否存在
    def switch_alert(self):
        r = self.is_alert()
        if not r:
            print("alert不存在")
        else:
            return r

    #鼠标悬停到元素
    def move_to_element(self, locator):
        """鼠标悬停操作"""
        if not isinstance(locator, tuple):
            raise LocatorTypeError("参数类型错误，locator必须是元祖类型：loc = ('id','value1')")
        ele = self.find(locator)
        ActionChains(self.driver).move_to_element(ele).perform()

    #定位元素后输入enter键
    def element_enter(self,locator):
        if not isinstance(locator, tuple):
            raise LocatorTypeError("参数类型错误，locator必须是元祖类型：loc = ('id','value1')")
        ele = self.find(locator)
        ele.send_keys(Keys.ENTER)

    #不定位元素输入enter键
    def no_element_enter(self):
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()

    #使用js点击元素
    def js_click(self,locator):
        if not isinstance(locator, tuple):
            raise LocatorTypeError("参数类型错误，locator必须是元祖类型：loc = ('id','value1')")
        ele = self.find(locator)
        #(arguments[0])就代表找到的button元素
        self.driver.execute_script("$(arguments[0]).click()",ele)


if __name__ == "__main__":
    #加载浏览器驱动
    driver = webdriver.Chrome()
    # 实例化
    web = Base(driver)
    #访问链接
    driver.get("https://www.baidu.com")
    loc_1 = ("id", "kw")
    web.send(loc_1, "hello")

    # Python is likely shutting down
    driver.close()