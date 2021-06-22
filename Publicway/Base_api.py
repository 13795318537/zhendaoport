# -*- coding: utf-8 -*-

import requests
from jsonpath import jsonpath


class Base_Api_syyA:
    # 封装request公共方法
    def send_data(self, data):
        print('成功使用send')
        return requests.request(**data)

    # 封装jsonpath公共方法
    def jsonpath_res(self, ojb, expr):
        return jsonpath(ojb, expr)
