import pytest
from pages.add_article_page import ArticleclassifyPage
import allure

from common.read_yml import ReadYaml
'''
allure对用例的等级划分成五个等级
 blocker　 阻塞缺陷（功能未实现，无法下一步）
 critical　　严重缺陷（功能点缺失）
 normal　　 一般缺陷（边界情况，格式错误）
 minor　 次要缺陷（界面错误与ui需求不符）
 trivial　　 轻微缺陷（必须项无提示，或者提示不规范）

'''

a = ReadYaml().readyaml()
# print(a['test_add_param_demo'])

testdata = a['test_add_param_demo']
# 测试数据单独拿出来
# testdata = [("测试中文", True),
#             ("test", True),
#             ("123456", True),
#             ]

# def test_add(login):
#     driver = login

@allure.epic("epic对大story的一个描述性标签")
@allure.feature("测试模块feature")
class TestAddXiangmu():

    @allure.testcase("http://49.235.92.12:8080/zentao/testcase-view-6-1.html")
    @allure.issue("http://49.235.92.12:8080/zentao/bug-view-1.html")
    @allure.story("用户故事1")
    @allure.title("用户标题1")
    @allure.severity("critical")
    def test_add_name_chinese(self,login):
        '''用例描述：添加新项目，名称是中文
        1.登录
        2.打开项目管理页面
        3.点击添加新项目，打开新添加页面
        4.输入项目名称，别名，描述，最后提交
        5.最后验证是否正常添加了项目
        '''
        driver = login
        edit = ArticleclassifyPage(driver)
        #点击打开项目管理
        edit.click_xiangmu()
        #添加新项目
        edit.add_new_xiangmu(name="我是中文名称03")
        #验证新项目是否添加成功
        res = edit.is_add_xiangmu_success("我是中文名称03")
        print("新项目是否添加成功：%s" % res)
        #断言
        assert res

    @allure.story("用户故事2")
    @allure.title("用户标题2")
    def test_add_name_english(self, login):
        '''用例描述：添加新项目，名称是英文
        1.登录
        2.打开项目管理页面
        3.点击添加新项目，打开新添加页面
        4.输入项目名称，别名，描述，最后提交
        5.最后验证是否正常添加了项目
        '''
        driver = login
        edit = ArticleclassifyPage(driver)
        # 点击打开项目管理
        edit.click_xiangmu()
        # 添加新项目
        edit.add_new_xiangmu(name="我是英文名称03")
        # 验证新项目是否添加成功
        res = edit.is_add_xiangmu_success("我是英文名称03")
        print("新项目是否添加成功：%s" % res)
        assert res



# @allure.feature("文章分类")
# class TestArticleclassify():
#
#     @allure.title("编辑文章分类，输入中文，编辑成功")
#     @allure.testcase("http://49.235.92.12:8080/zentao/testcase-view-6-1.html")
#     def test_add_article1(self, login):
#         '''用例描述：1.先登陆
#         点文章分类导航标签
#         编辑页面输入，分类名称，如:文学
#         点保存按钮'''
#         driver = login
#         edit = ArticleclassifyPage(driver)
#         edit.click_classify_nav()
#         edit.edit_classify("测试xxx")
#         res2 = edit.is_edit_classify_success("测试xxx")
#         print("编辑是否成功：%s"%res2)
#         assert res2
#
#     @allure.severity("critical")
#     @allure.title("编辑文章分类-输入重复的分类，保存失败，不能添加重复的")
#     @allure.testcase("http://49.235.92.12:8080/zentao/testcase-view-5-1.html")
#     @allure.issue("http://49.235.92.12:8080/zentao/bug-view-1.html")
#     def test_add_article2(self, login):
#         '''用例描述：1.先登陆
#         点文章分类导航标签
#         重新打开编辑页，输入：计算机
#         再次点保存按钮'''
#         driver = login
#         edit = ArticleclassifyPage(driver)
#         edit.click_classify_nav()
#         edit.edit_classify("测试xxx")
#         res2 = edit.is_edit_classify_success("测试xxx")
#         print("编辑是否成功：%s" % res2)
#         assert res2
#
#     @pytest.mark.parametrize("test_input, expected", testdata)
#     def test_add_param_demo(self, login, test_input, expected):
#         '''用例描述：1.先登陆
#         点文章分类导航标签
#         编辑页面输入，分类名称，如:文学
#         点保存按钮'''
#         driver = login
#         edit = ArticleclassifyPage(driver)
#         edit.click_classify_nav()
#         edit.edit_classify(test_input)
#         res2 = edit.is_edit_classify_success(test_input)  # 实际结果
#         print("编辑是否成功：%s" % res2)
#         assert res2 == expected