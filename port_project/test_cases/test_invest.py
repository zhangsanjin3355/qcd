# @Time : 2019/7/26 14:07 
# @Author : zhangsanjin
# @File : test_invest.py
# @Software: PyCharm
import unittest
from port_project.common.do_excel import DoExcel
from port_project.common import project_path
from port_project.common.http_request import HttpRequest
from ddt import ddt, data
from port_project.common.get_data_common import GetData
from port_project.common.do_mysql import DoMysql

# 测试数据test_data
test_data = DoExcel(project_path.case_path).read_data("invest", "InvestCASE")  # 列表
print("测试数据是",test_data)

# COOKIES=None  #初始化cookies为None
@ddt
class TestInvest(unittest.TestCase):
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
        if case["Params"].find("loan_id") != -1:  # 找到了替换
            param = eval(case["Params"].replace("loan_id", str(getattr(GetData, "LOAN_ID"))))# 反射拿到是int类型，替换要强转字符串
        else:
            param = eval(case["Params"])
            print("获得的params是",param)

        #判断投资前的账户余额
        if case["sql"]!=None:  #找到sql了
            before_amount=DoMysql().do_mysql(eval(case["sql"])["sql"])[0]  #投资前金额case["sql"]是字符串，eval后字典
            print("投资前金额是",before_amount)
        print("----正在测试{}模块里面的第{}条测试用例：用例名称是：{}----".format(case["Module"], case["CaseId"], case["Title"]))
        resp = HttpRequest().http_request(method, url, param, cookies=getattr(GetData, "COOKIES"))
        # 判断cookies是否为空
        if resp.cookies:
            setattr(GetData, "COOKIES", resp.cookies)  # 把得到的cookies反射回getdata,cookies属性

        # 断言
        try:
            self.assertEqual(eval(case["ExpectedResult"]), resp.json())  # json无序
            #在加一个断言，当有sql的时候执行
            if case["sql"]!=None:
                # 判断投资后的账户余额
                after_amount = DoMysql().do_mysql(eval(case["sql"])["sql"])[0] # 投资前金额case["sql"]是字符串，eval后字典
                invest_amount = param["amount"]  #投资金额
                expect_amount= before_amount - invest_amount
                self.assertEqual(expect_amount,after_amount)  #断言：判断投资金额和余额是否匹配
            TestResult = "Pass"
            print("这条是通过")
        except AssertionError as e:
            print("测试用例的错误是：{}".format(e))
            TestResult = "Failed"
            raise e
        finally:
            # 写回测试结果
            self.t.write_back("invest", case["CaseId"] + 1, 9, resp.text)  # 写回响应结果
            self.t.write_back("invest", case["CaseId"] + 1, 10, TestResult)  # 写回测试结论
