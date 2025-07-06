import logging
import pytest
from jinja2 import Template
from allure_utils import allure_init
from asserts import http_assert, jdbc_assert
from extractor import json_extractor, jdbc_extractor
from send_request import send_http_request
from utils.excel_utils import read_excel
from analyse_case import analyse_case


class TestRunner:
    # 读取用例数据，结果为dict
    data = read_excel()
    # 全局变量字典置空
    global_var = {}

    @pytest.mark.parametrize("case", data)
    def test_case(self, case):
        # 渲染case模板
        case = eval(Template(str(case)).render(self.global_var))

        # 0.输出日志信息
        logging.info(f'ID:{case["id"]},模块：{case["feature"]},'
                     f'场景：{case["story"]},标题：{case["title"]}')

        # 1.初始化allure参数
        allure_init(case=case)

        # 2.解析请求数据
        requests_data = analyse_case(case)

        # 3.发送请求
        res = send_http_request(**requests_data)

        # 4.HTTP&JDBC断言
        http_assert(case, res)
        jdbc_assert(case, res)

        # 5.JSON&JDBC提取
        json_extractor(case, res, self.global_var)
        jdbc_extractor(case, self.global_var)
