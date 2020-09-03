#coding=utf8


import unittest
from utils.http_method import Method
from data.analyze_data_4 import Analyze
import json
from ddt import ddt,data,unpack


@ddt
class TestMethod(unittest.TestCase):

    get_data = Analyze()
    data_all = get_data.analyze_data()


    def setUp(self):
        self.run = Method()

    @data(data_all[0])
    @unpack
    def test_01_register(self,*args):
        #args[3]中含有中文，将字符串转为二进制
        res = self.run.send_request(args[0],args[1],args[2],args[3].encode('utf-8'))
        # print(res)
        self.assertDictContainsSubset(json.loads(args[4]),res,msg="测试用例失败")



    @data(data_all[1])
    @unpack
    def test_02_login(self,*args):
        res = self.run.send_request(args[0],args[1],args[2],args[3])
        # print(res)
        global UserID
        UserID = res['ResultObj']['UserID']
        self.assertDictContainsSubset(json.loads(args[4]),res['ResultObj'],msg="测试用例失败")
        return res

    @data(data_all[2])
    @unpack
    def test_03_up_apikey(self,*args):
        res_dict3 = json.loads(args[3])
        res_dict3['OperUserID'] = res_dict3['UserID'] = UserID
        res= self.run.send_request(args[0],args[1],args[2],res_dict3)
        # print(res)
        self.assertDictContainsSubset(json.loads(args[4]),res,msg="测试用例失败")



    @data(data_all[3])
    @unpack
    def test_04_login_again(self,*args):
        res = self.run.send_request(args[0],args[1],args[2],args[3])
        # print(res)
        global Token
        Token = res['ResultObj']['AccessToken']
        self.assertDictContainsSubset(json.loads(args[4]),res['ResultObj'],msg="测试用例失败")


    @data(data_all[4])
    @unpack
    def test_05_new_project(self,*args):
        global res_dict2
        res_dict2 = json.loads(args[2])
        res_dict2['AccessToken'] = Token
        res = self.run.send_request(args[0],args[1],res_dict2,args[3])
        # print(res)
        global ProjectID
        ProjectID = res['ResultObj']
        self.assertDictContainsSubset(json.loads(args[4]),res,msg="测试用例失败")


    @data(data_all[5])
    @unpack
    def test_06_new_device(self,*args):
        res_dict3 = json.loads(args[3])
        res_dict3['ProjectIdOrTag'] = str(ProjectID)
        res = self.run.send_request(args[0],args[1],res_dict2,res_dict3)
        # print(res)
        global deviceId1
        deviceId1 = res['ResultObj']
        self.assertDictContainsSubset(json.loads(args[4]),res,msg="测试用例失败")

    @data(data_all[6])
    @unpack
    def test_07_new_sensor(self,*args):
        str0 = args[0].replace("{deviceId}",str(deviceId1))
        res = self.run.send_request(str0,args[1],res_dict2,args[3])
        # print(res)
        self.assertDictContainsSubset(json.loads(args[4]),res,msg="测试用例失败")

    @data(data_all[7])
    @unpack
    def test_08_new_actor(self,*args):
        str0 = args[0].replace("{deviceId}",str(deviceId1))
        res = self.run.send_request(str0,args[1],res_dict2,args[3])
        # print(res)
        self.assertDictContainsSubset(json.loads(args[4]),res,msg="测试用例失败")

    @data(data_all[8])
    @unpack
    def test_09_delete_project(self,*args):
        str3 = args[3].replace("{ProjectId}",str(ProjectID))
        res = self.run.send_request(args[0],args[1],res_dict2,str3)
        # print(res)
        self.assertDictContainsSubset(json.loads(args[4]),res,msg="测试用例失败")


if __name__ == "__main__":
    unittest.main(verbosity=2)





