#!/usr/bin/python3
#-*- coding:utf-8 -*-
#@Time   :2019/3/1 10:05
#@Author :zhang_san_jin
#@Email  :358405442@qq.com
#@Fale   :class_my_log.py
#1：编写一个日志类，能够实现输出文件到指定文件和console
import logging
#from week_7.class_0227.class_0225__config import ReadConfig
from API_6.common import project_path
class MyLog:
    def __init__(self):
        '''读取配置文件找到相应数据
        logger_name：日志管理器名字
        logger_level：收集级别
        file_name：输出指定文件日志名
        file_level：文件-输出级别
        stream_level：控制台-输出级别
        log_formatter：输出日志格式'''
        # self.logger_name=ReadConfig("log.conf").get_str("LOG","logger_name")
        # self.logger_level=ReadConfig("log.conf").get_str("LOG","logger_level")
        # self.file_name=ReadConfig("log.conf").get_str("LOG","file_name")
        # self.file_level=ReadConfig("log.conf").get_str("LOG","file_level")
        # self.stream_level = ReadConfig("log.conf").get_str("LOG", "stream_level")
        # self.log_formatter=ReadConfig("log.conf").get_str("LOG", "log_formatter")
    def my_log(self,level,msg):
        my_logger=logging.getLogger("aip_log") #定义日志收集器的名字
        my_logger.setLevel("DEBUG") #定义收集级别
        #格式化打印信息
        formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s')

        #输出渠道控制台
        ch = logging.StreamHandler()
        ch.setLevel("DEBUG")        #输出级别
        ch.setFormatter(formatter)  #把格式化信息输出到控制台
        my_logger.addHandler(ch)    #收集器与输出渠道对接

        #输出渠道指定文件
        fh = logging.FileHandler(project_path.log_path,encoding="utf-8")   #日志名，编码
        fh.setLevel("DEBUG")        #输出级别
        fh.setFormatter(formatter)  #把格式化信息输出到指定文件
        my_logger.addHandler(fh)    #收集器与输出渠道对接
        #日志级别信息
        if level=="DEBUG":
           my_logger.debug(msg)
        elif level=="INFO":
            my_logger.info(msg)
        elif level=="WARNING":
            my_logger.warning(msg)
        elif level=="ERROR":
            my_logger.error(msg)
        else:
            my_logger.critical(msg)
        #关闭输出渠道
        my_logger.removeHandler(ch)
        my_logger.removeHandler(fh)
    #以下是可以优化的地方
    def debug(self, msg):
        self.my_log("DEBUG",msg)
    def info(self, msg):
        self.my_log("INFO",msg)
    def warning(self, msg):
        self.my_log("WARNING",msg)
    def error(self, msg):
        self.my_log("ERROR",msg)
    def critical(self, msg):
        self.my_log("CRITICAL",msg)



if __name__ == '__main__':
    my_logger=MyLog()
    #my_logger.debug("debug的日志信息")
    #my_logger.info("info的日志信息")

#优化：指定级别，可配置
