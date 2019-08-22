# @Time : 2019/7/26 14:07 
# @Author : zhangsanjin
# @File : test_loan_add.py
# @Software: PyCharm
import unittest
from port_project.common.do_excel import DoExcel
from port_project.common import project_path
from port_project.common.http_request import HttpRequest
from ddt import ddt, data
from port_project.common.get_data_common import GetData
from port_project.common import get_data_common
from port_project.common.do_mysql import DoMysql

# 测试数据test_data
test_data = DoExcel(project_path.case_path).read_data("add_loan", "AddLoanCASE")  # 列表


# COOKIES=None  #初始化cookies为None
@ddt
class TestLoanAdd(unittest.TestCase):
    def setUp(self):
        self.t = DoExcel(project_path.case_path)  # 对象属性。定位操作表单

    def tearDown(self):
        pass

    @data(*test_data)
    def test_case(self, case):
        # case 字典
        global TestResult  # 全局变量,测试结果
        # 执行测试
        method = case["Method"]
        url = case["Url"]
        # 替换参数中ID的值
        #老方法
        # if case["Params"].find("loan_id") != -1:  # 找到了替换
        #     param = eval(case["Params"].replace("loan_id", str(getattr(GetData, "LOAN_ID"))))# 反射拿到是int类型，替换要强转字符串
        # else:
        #     param = eval(case["Params"])

        #正则表达式替换，mobilephone、pwd、memberId
        param = eval(get_data_common.replace(case["Params"]))


        print("----正在测试{}模块里面的第{}条测试用例：用例名称是：{}----".format(case["Module"], case["CaseId"], case["Title"]))
        resp = HttpRequest().http_request(method, url, param, cookies=getattr(GetData, "COOKIES"))
        # 判断cookies是否为空
        if resp.cookies:
            setattr(GetData, "COOKIES", resp.cookies)  # 把得到的cookies反射回getdata,cookies属性
        # 判断用例表sql字段是否有值，需要连接数据库
        if case["sql"] != None:  # 不为空，就进行连接数据库执行sql
            loan_id = DoMysql().do_mysql(eval(case["sql"])["sql"])  # 返回的是元组类型
            setattr(GetData,"loan_id", str(loan_id[0]))  # 反射标的id,根据索引拿到id值，是int类型
            print(getattr(GetData,"loan_id"))
        # 断言
        try:
            self.assertEqual(eval(case["ExpectedResult"]), resp.json())  # json无序
            TestResult = "Pass"
            print("这条是通过")
        except AssertionError as e:
            print("测试用例的错误是：{}".format(e))
            TestResult = "Failed"
            raise e
        finally:
            # 写回测试结果
            self.t.write_back("add_loan", case["CaseId"] + 1, 9, resp.text)  # 写回响应结果
            self.t.write_back("add_loan", case["CaseId"] + 1, 10, TestResult)  # 写回测试结论
