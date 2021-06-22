# -*- coding: utf-8 -*-

import allure
import pytest
import os
import yaml
from zhendaoport.syyA.Member_management.member_management import Member_api_A

# 测试前打开yaml文件
yaml_file_path = os.path.dirname(__file__) + "/memberdata.yaml"
# 从文件中获取数据
with open(yaml_file_path, encoding='utf-8') as f:
    memberdata = yaml.safe_load(f)
    member_list_data = memberdata['member_list']['member_list_data']
    member_list_myid = memberdata['member_list']['myid']


@allure.feature('会员列表')
class Test_smoke1:
    def setup_class(self):
        print("开始")
        conf = yaml.safe_load(open("memberdata.yaml", encoding='utf-8'))
        acc_token = conf["token"]
        self.member_list = Member_api_A(acc_token)
        print("结算")

    @pytest.mark.parametrize(
        ("url", "page", "size", "typenum", "export", "username", "level", "start_time", "end_time", "tel",
         "twitter_info",
         "super_shop_name", "contpage"),
        member_list_data,
        ids=member_list_myid)
    def test_s1(self, url, page, size, typenum, export, username, level, start_time, end_time, tel, twitter_info,
                super_shop_name, contpage):
        # self.member_list = Member_api_A()
        r = self.member_list.member_list_A(url, page, size, typenum, export, username, level, start_time, end_time, tel,
                                           twitter_info, super_shop_name)
        print(r)
        check_list = self.member_list.jsonpath_res(r, "$..member_id")
        print(check_list)
        assert contpage in check_list
        assert r['code'] == 200
