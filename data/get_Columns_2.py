#封装获取列号方法，以后维护方便一些(目的：获取id，url，请求方法，是否运行，预算结果等所在excel中的列号)
class global_var:
    id = 0
    case_name = 1
    URL = 2
    request_way = 3
    header = 4
    json_data = 5
    exspect = 6





#获取id所在列号
def id_colnum():
    return global_var.id

#获取case_name所在列号
def case_name_colnum():
    return global_var.case_name


#获取URL所在列号
def URL_colnum():
    return global_var.URL

#获取request_way所在列号
def request_way_colnum():
    return global_var.request_way

#获取header所在列号
def header_colnum():
    return global_var.header

#获取json_data所在列号
def json_data_colnum():
    return global_var.json_data

#获取respect所在列号
def exspect_colnum():
    return global_var.exspect
