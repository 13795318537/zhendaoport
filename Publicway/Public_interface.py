import json
from Publicway.Base_api import Base_Api_syyA


class Public_interf(Base_Api_syyA):

    def __init__(self, acc_token):
        self.token = self.get_token(acc_token)

    def get_token(self, acc_token):
        data = {'method': 'post',
                'url': 'http://devsyy002.presyy.nbseo.cn/baseapi/platform/auth/login',
                'headers': {'Content-Type': 'application/json'
                            },
                'json': {
                    'isFalse': '0',
                    'token': acc_token}
                }
        print(data)
        r = self.send_data(data)
        print(r.json())
        return r.json()['data']["access_token"]
