# @Time : 2019/7/26 14:07 
# @Author : zhangsanjin
# @File : test_recharge.py 
# @Software: PyCharm
import unittest
from port_project.common.do_excel import DoExcel
from port_project.common import project_path
from port_project.common.http_request import HttpRequest
from ddt import ddt,data
from port_project.common.get_data_common import GetData
from port_project.common.do_mysql import DoMysql
#测试数据test_data
test_data = DoExcel(project_path.case_path).read_data("recharge","RechargeCASE")
# COOKIES=None  #初始化cookies为None
@ddt
class TestRecharge(unittest.TestCase):
    def setUp(self):
        self.t = DoExcel(project_path.case_path) #对象属性。定位操作表单

    def tearDown(self):
        pass
    @data(*test_data)
    def test_case(self,case):
        global TestResult #全局变量,测试结果
        # global COOKIES
        # 执行测试
        method = case["Method"]
        url = case["Url"]
        param = eval(case["Params"])
        #充值前查询数据库获取账户余额
        if case["sql"] is not None:
            before_amount=DoMysql().do_mysql(eval(case["sql"])["sql"])[0]  #充值前金额case["sql"]是字符串，eval后字典
            print("充值前金额是",before_amount)
        print("----正在测试{}模块里面的第{}条测试用例：用例名称是：{}----".format(case["Module"], case["CaseId"], case["Title"]))
        resp = HttpRequest().http_request(method, url, param,cookies=getattr(GetData,"COOKIES")) #获取反射属性
        #判断cookies是否为空
        if resp.cookies:
            setattr(GetData,"COOKIES",resp.cookies) #把得到的cookies反射回getdata,cookies属性
        #断言
        try:
            # 断言：充值后金额=充值前+充值金额
            if case["sql"] is not None:
                after_amount = DoMysql().do_mysql(eval(case["sql"])["sql"])[0]  # 充值后金额
                recharge_amount = int(param["amount"])  # 充值金额
                expect_amount = before_amount + recharge_amount #充值后金额=充值前+充值  int
                self.assertEqual(expect_amount, after_amount)
                print("充值成功数据比对成功！！！！！！")
            #如果充值成功，期望结果取期望结果
            if case["ExpectedResult"].find("expect_amount") > -1:
                case["ExpectedResult"] = case["ExpectedResult"].replace("expect_amount",str(expect_amount))
            self.assertEqual(eval(case["ExpectedResult"]),resp.json())  #json无序

            TestResult = "Pass"
            print("这条是通过")
        except AssertionError as e:
            print("测试用例的错误是：{}".format(e))
            TestResult = "Failed"
            raise e
        finally:
            # 写回测试结果
            self.t.write_back("recharge",case["CaseId"] + 1, 9, resp.text)  # 写回响应结果
            self.t.write_back("recharge",case["CaseId"] + 1, 10, TestResult)  # 写回测试结论
