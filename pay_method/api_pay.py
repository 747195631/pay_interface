# coding:utf-8
from urllib import parse
import requests
from common.util.Md5 import Md5
import simplejson

#测试环境接口地址
url1 = 'http://test2.ishop-city.com/cashier/wechat/micropay'
#开发环境接口地址
# url1 = 'http://plat.ishop-city.com/cashier/wechat/micropay'
data1 = {'body': 'Ipad mini 16G 白色',
         # 'detail': 'Ipad mini 16G 白色',
         'total_fee': '1',
         'auth_code': '130016744277440153',
         'mcode': 'hpm2',  #测试环境
         # 'mcode': 'xiaoyueb',  #开发环境
         'mallId': '158',   #测试环境
         # 'mallId': '11668',  #开发环境
         'receiveMoneyName': '123456',
         'cashSn': '123456',
         'noteNo': '123456',
         'cashOperator': '123456',
         'token_id': '20150811160250905707266',
         # 'sign': '06963b57fd5911e5b28b5254969e155c'
         }

def sign_deal(data, key):
    data_sort = sorted(data.items(), key=lambda asd: asd[0], reverse=False)
    sign = Md5.md5(splice_str(data_sort, key))
    print(sign)
    data['sign'] = sign
    print(data)
    return data


def splice_str(data_list, key):
    num = 0
    sign_str = ""
    for i in data_list:
        if num == len(data_list) - 1:
            sign_str = sign_str + i[0] + "=" + i[1]
        else:
            sign_str = sign_str + i[0] + "=" + i[1] + "&"
        num += 1
    sign_str = sign_str + "&" + "key" + "=" + key
    return sign_str


headers = {'content-type': 'application/x-www-form-urlencoded;charset=utf-8'}
responses_object = requests.post(url=url1, data=sign_deal(data1, "6510753af0dd1a3c26db9c43896b3932"), headers=headers)
print(responses_object.json())

