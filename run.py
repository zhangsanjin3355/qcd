# @Time : 2019/7/23 14:56 
# @Author : zhangsanjin
# @File : run.py 
# @Software: PyCharm
#执行测试用例，生成测是报告
import HTMLTestRunnerNew
from port_project.common import project_path # 路径
from port_project.test_cases.test_register import TestRegister   #执行用例的代码(注册)
from port_project.test_cases.test_recharge import TestRecharge   #执行用例的代码(充值)
from port_project.test_cases.test_loan_add import TestLoanAdd    #执行用例的代码(加标)
from port_project.test_cases.test_invest import TestInvest       #执行用例的代码(投资)
import unittest
import sys
sys.path.append("./")  #追加上一级目录

# print(sys.path)

#创建一个测试集
suite=unittest.TestSuite()
#添加用例
loader=unittest.TestLoader()#载入器
# suite.addTest(loader.loadTestsFromTestCase(TestRegister))#添加用例
# suite.addTest(loader.loadTestsFromTestCase(TestRecharge))
suite.addTest(loader.loadTestsFromTestCase(TestLoanAdd))
#执行用例，生成测试报告
#写入文件


with open(project_path.report_path,"wb") as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                              verbosity=2,
                                              title="test_report_zx",
                                              description="test_report_zx",
                                              tester="zhangsanjin_test")
    runner.run(suite)   #执行用例，传入测试用例集,生成测试报告







