import pytest
import requests
import logging
import allure_pytest

from excel_utils import read_excel


class TestRunner:
    # 读取测试数据
    data = read_excel()
    # logging.basicConfig(level=logging.INFO)
    @pytest.mark.parametrize("case", data)
    def test_case(self, case):
        logging.info(case)
        # 设置url参数
        method = case['method']
        url = 'http://192.168.10.131:8888/api/private/v1' + case['path']
        data=eval(case['data']) if isinstance(case['data'],str) else None
        params=eval(case['params']) if isinstance(case['params'],str) else None
        json=eval(case['json']) if isinstance(case['json'],str) else None
        files=eval(case['files']) if isinstance(case['files'],str) else None
        headers=eval(case['headers']) if isinstance(case['headers'],str) else None
        requests_data={
            'method':method,
            'url':url,
            'data':data,
            'params':params,
            'json':json,
            'files':files,
            'headers':headers
        }
        res=requests.request(**requests_data)
        print(res.json())
        assert case['expected']==res.json()['meta']['msg']
