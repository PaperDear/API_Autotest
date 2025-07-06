import allure
import jsonpath
import logging
from send_request import send_jdbc_request

"""
此处使用的是用例的jsonExData，例如{"token":"$.data.token"}
token为需要提取的值，$.data.token通过jsonpath提取到响应内所需的值
提取后将两个值通过键值对的方式存入all字典内
"""
def json_extractor(case,res,global_var,index=0):
    if case['jsonExData']:
        with allure.step("JSON提取"):
            # case['jsonExdata']提取到的是字符串，需要转为字典类型
            for key, value in eval(case['jsonExData']).items():
                value = jsonpath.jsonpath(res.json(), value)[0]
                # 写入全局变量字典内
                global_var[key] = value
            logging.info(f"4.JSON提取，根据{case['jsonExData']}提取参数，全局变量更新：({global_var})")
            allure.attach(f"{global_var}","JSON提取后全局变量")

def jdbc_extractor(case,global_var):
    # 数据库提取
    if case['sqlExData']:
        # sqlExData内为参数名:SQL语句
        with allure.step("数据库提取"):
            for key, value in eval(case['sqlExData']).items():
                value = send_jdbc_request(value)
                # 写入全局变量字典内
                global_var[key] = value
        logging.info(f"4.JBDC提取，根据{case['sqlExData']}提取参数，全局变量字典更新：({global_var})")
        allure.attach(f"{global_var}", "数据库提取后全局变量")
