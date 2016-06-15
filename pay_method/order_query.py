#coding:utf-8
from urllib import parse
import requests
from common.util.Md5 import Md5

url1='http://test2.ishop-city.com/cashier/pad/nativePayQuery.htmlx'
data1={'trade_id':'20160614165211042632583'}   #输入商户订单号
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
    sign_str = sign_str + "&" + "pad_key" + "=" + key
    return sign_str


headers = {'content-type': 'application/x-www-form-urlencoded;charset=utf-8'}
responses_object = requests.post(url=url1, data=sign_deal(data1, "4E34SrAxc019y4d67692Fy34A6716s1d"), headers=headers)
print(responses_object.json())