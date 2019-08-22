# @Time : 2019/7/23 17:25 
# @Author : zhangsanjin
# @File : project_path.py 
# @Software: PyCharm
#所有文件的路径
import os

#项目底层路径
project_path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
print(project_path)
#测试用例路径
case_path=os.path.join(project_path,"test_cases","test_api.xlsx")
print(case_path)
#测试报告路径
report_path=os.path.join(project_path,"test_result","test_report","test_report.html")
print(report_path)
#日志路径
log_path=os.path.join(project_path,"test_result","test_log","test_report.html")
#配置文件路径
conf_path=os.path.join(project_path,"conf","case.conf")