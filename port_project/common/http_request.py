# @Time : 2019/7/19 15:34 
# @Author : xx
# @File : http_request.py
# @Software: PyCharm

import requests
class HttpRequest:
    '''完成http的get或post请求，并返回响应结果'''
    def http_request(self,method,url,param,cookies):
        global resp
        if method.upper()=="GET":
            try:
                resp=requests.get(url,params=param,cookies=cookies)
            except Exception as e:
                print("get请求出错了:{}".format(e))
        elif method.upper()=="POST":
            try:
                resp=requests.post(url,data=param,cookies=cookies)
            except Exception as e:
                print("post请求出错了:{}".format(e))
        else:
            print("不支持该种方式")
            resp=None
        return resp
if __name__ == '__main__':
    url =r"http://test.lemonban.com/futureloan/mvc/api/member/register"
    param={"mobilephone":15311112222,"pwd":""}
    resp = HttpRequest().http_request("post",url,param)
    print(resp)


