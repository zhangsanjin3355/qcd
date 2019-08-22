# @Time : 2019/7/24 10:26 
# @Author : zhangsanjin
# @File : test_register.py
# @Software: PyCharm
import unittest
from port_project.common.do_excel import DoExcel
from port_project.common import project_path
from port_project.common.http_request import HttpRequest
from ddt import ddt,data
#测试数据test_data
test_data = DoExcel(project_path.case_path).read_data("register","RegisterCASE")
@ddt
class TestRegister(unittest.TestCase):
    def setUp(self):
        self.t = DoExcel(project_path.case_path) #对象属性。定位操作表单

    def tearDown(self):
        pass
    @data(*test_data)
    def test_case(self,case):
        global TestResult #全局变量
        # 执行测试
        method = case["Method"]
        url = case["Url"]
        param = eval(case["Params"])
        print("----正在测试{}模块里面的第{}条测试用例：用例名称是：{}----".format(case["Module"], case["CaseId"], case["Title"]))
        resp = HttpRequest().http_request(method, url, param,cookies=None)
        #断言
        try:
            self.assertEqual(eval(case["ExpectedResult"]),resp.json())  #json无序
            TestResult = "Pass"
        except AssertionError as e:
            print("测试用例的错误是：{}".format(e))
            TestResult = "Failed"
            raise e
        finally:
            # 写回测试结果
            self.t.write_back("register",case["CaseId"] + 1, 9, resp.text)  # 写回响应结果
            self.t.write_back("register",case["CaseId"] + 1, 10, TestResult)  # 写回测试结论
