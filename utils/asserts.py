import jsonpath
import allure
import logging

from send_request import send_jdbc_request


@allure.step("http响应断言")
def http_assert(case, res, index=0):
    if case['check']:
        # jsonpath()返回的是一个列表，需要取索引值
        res_json = jsonpath.jsonpath(res.json(), case['check'])[index]
        logging.info(f"3.http响应断言，实际结果:({res_json})==预期结果:({case['expected']})")
        assert (res_json == case['expected'])
    else:
        logging.info(f"3.http响应断言，预期结果:({case['expected']}) in 实际结果：({res.text})")
        # case获取到的是字符串，不能判断是否在字典res.json()中，可以通过text文本判断包含关系
        assert case['expected'] in res.text


def jdbc_assert(case, res):
    if (case['sql_check'] and case['sql_expected']):
        res_jdbc = send_jdbc_request(case["sql_check"])
        with allure.step("数据库断言"):
            logging.info(f"3.数据库断言，实际结果:({res_jdbc})==预期结果:({case['sql_expected']})")
            assert res_jdbc == case['sql_expected']
