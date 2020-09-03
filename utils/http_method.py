#coding=utf8

import requests,json

class Method:


    #post、put、delete封装
    #注意:get如果不传data的话，注意写先定义好data＝None，然后注意参数顺序，data＝None放在最后的位置。
    def send_request(self,url,method,headers,data=None):
        if (type(headers) == str):
            headers = json.loads(headers)
        if (type(data) == dict):
            data = json.dumps(data)

        res_str = None
        if method == "post":
            res_str = requests.post(url=url,headers=headers,data=data)
        elif method == "put":
            res_str = requests.put(url=url,headers=headers,data=data)
        else:
            res_str = requests.delete(url=url,headers=headers,data=data)

        res_dict = json.loads(res_str.content)
        return res_dict

