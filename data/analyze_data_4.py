#对数据进行解析处理组合得到有效数据，并执行熨平

from data import get_Columns_2,get_data_3
import json



class Analyze:


    #对获取到的数据进行解析处理,并执行用例。
    def analyze_data(self):
        raw_data = get_data_3.GetData(0).data()
        arr_list = []
        for i in range(0,len(raw_data)):
            request_url = raw_data[i][get_Columns_2.URL_colnum()]
            request_way = raw_data[i][get_Columns_2.request_way_colnum()]
            request_header = raw_data[i][get_Columns_2.header_colnum()]
            request_data = raw_data[i][get_Columns_2.json_data_colnum()]
            #去除字符串中的换行符\n和多余的空格
            request_data = request_data.replace('\n','').replace(' ','')
            request_expect = raw_data[i][get_Columns_2.exspect_colnum()]
            arr_list.append([request_url,request_way,request_header,request_data,request_expect])

        # print(arr_list[2])
        # print(type(arr_list))

        return arr_list



if __name__ == '__main__':
    s = Analyze()
    s.analyze_data()


