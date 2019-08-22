# @Time : 2019/7/31 14:16 
# @Author : zhangsanjin
# @File : get_data.py 
# @Software: PyCharm
from port_project.common import read__config_common
from port_project.common import project_path
import re


class GetData:
    config = read__config_common.ReadConfig(project_path.conf_path)  # 读取配置文件的对象
    COOKIES = None
    LOAN_ID = None  # 新添加标的id
    normal_user = config.get_str("user_data", "normal_user")
    normal_pwd = config.get_str("user_data", "normal_pwd")
    normal_member_id = config.get_str("user_data", "normal_member_id")

# 正则表达式，参数化替换
# 模块函数
def replace(target):
    p1 = "#(.*?)#"   #正则表达式
    while re.search(p1, target):  # 循环检查参数中是否能匹配到正则表达式
        m = re.search(p1, target)  # 取出符合的对象 -->组 #normal_user#
        key = m.group(1)  # 按组取出，normal_user
        value = getattr(GetData, key)  # 使用反射取到需要替代的值
        target = re.sub(p1, value, target, count=1)  # 正则的sub方法进行替换
    return target
