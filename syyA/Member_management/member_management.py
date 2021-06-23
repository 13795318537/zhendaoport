# -*- coding: utf-8 -*-

from Publicway.Public_interface import Public_interf


class Member_api_A(Public_interf):
    def member_list_A(self, url, page, size, typenum, export, username, level, start_time, end_time, tel, twitter_info,
                      super_shop_name):
        date = {'method': 'get',
                'url': url,
                'headers': {'access-token': self.token
                            # 'X-Token': 'r2gHSqj28Ms3kS3zWMsnlRhPEJqwfO8e'
                            },
                'params': {
                    "page": page,
                    "size": size,
                    "type": typenum,
                    "export": export,
                    "username": username,
                    "level": level,
                    "start_time": start_time,
                    "end_time": end_time,
                    "tel": tel,
                    "twitter_info": twitter_info,
                    "super_shop_name": super_shop_name
                }
                }
        print('会员列表发送')
        r = self.send_data(date)
        return r.json()
