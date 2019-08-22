#!/usr/bin/python3
#-*- coding:utf-8 -*-
#@Time   :2019/2/26 11:43
#@Author :zhang_san_jin
#@Email  :358405442@qq.com
#@Fale   :class_0225_data_con.py
from configparser import ConfigParser

class ReadConfig:
    def __init__(self,file_name):  #file_name配置文件的路径
        self.cf=ConfigParser()  #实例化一个对象
        try:
            self.cf.read(file_name,encoding="utf-8")
        except Exception as e:
            print("文件打开报错：{}".format(e))
    '''用不同方法读取配置文件中的数据类型'''
    def get_init(self,section,option):
        '''读取整数'''
        try:
            value = self.cf.getint(section,option)
            return value
        except Exception as e:
            print("取值报错-整数类型：{}".format(e))
    def get_float(self,section,option):
        '''读取浮点数'''
        try:
            value = self.cf.getfloat(section,option)
            return value
        except Exception as e:
            print("取值报错-浮点数类型：{}".format(e))
    def get_bool(self,section,option):
        '''读取布尔值'''
        try:
            value = self.cf.getboolean(section,option)
            return value
        except Exception as e:
            print("取值报错-布尔值类型：{}".format(e))
    def get_str(self,section,option):
        '''读取字符串'''
        try:
            value = self.cf.get(section,option)
            return value
        except Exception as e:
            print("取值报错-字符串类型：{}".format(e))
    def get_data(self,section,option):
        '''读取其他数据类型-列表列表、字典、元组'''
        try:
            value = self.cf.get(section,option)
            return eval(value)  #打印本身数据类型
        except Exception as e:
            print("取值报错-其他类型：{}".format(e))

if __name__ == '__main__':
    from API_3.common import project_path
    res=(ReadConfig(project_path.conf_path).get_data("CASE","case_id"))   #布尔值
    print(res)
    #cf.read("python_zx1.conf", encoding="utf-8")
    # cf.read_init()   #整数
    # cf.read_float()  #浮点数
    # cf.read_bool()   #布尔值
    # cf.read_str()    #字符串
    #cf.read_type()   #列表、字典、元组

#配置文件数据
# [StudentName]
# #存储学生的信息
# stu_1=nancy
# stu_2=9527
# stu_3=张鑫
# stu_4=3.14
# stu_5=[1,2,3]
# stu_6=True
# stu_7={"name":"zx","age":10}
# stu_8=(1,2,3)