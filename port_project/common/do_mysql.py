# @Time : 2019/8/1 10:57 
# @Author : zhangsanjin
# @File : do_mysql.py
# @Software: PyCharm
from mysql import connector
import pymysql
from port_project.common.read__config_common import ReadConfig
from port_project.common import project_path
class DoMysql:
    '''操作数据的库的类，进行数据库的读取'''
    def do_mysql(self,query,flag=1):
        '''
        :param query: sql查询语句
        :param flag: 1获取一条数据 2获取多条数据
        :return:
        '''
        db_config=ReadConfig(project_path.conf_path).get_data('DB','db_config')
        cnn = pymysql.connect(**db_config) #建立连接
        cursor = cnn.cursor()  #创建游标
        cursor.execute(query)  #执行sql
        if flag==1:
            res = cursor.fetchone()
        else:
            res = cursor.fetchall()
        return res
if __name__ == '__main__':
    query = 'select Id from loan where MemberID<1240'
    res=DoMysql().do_mysql(query,2)
    print("数据库的查询结果是：{}".format(res))

    # 113255


