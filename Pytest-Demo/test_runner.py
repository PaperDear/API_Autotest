import pytest
import requests

data = [
    {
        "method": "post",
        "url": "http://192.168.10.131:8888/api/private/v1/login",
        "params": None,
        "data": {
            "username": "admin","password": "123456",
        },
        "json": None,
        "files": None,
        "headers": None
    },
    {
        "method": "get",
        "url": "http://192.168.10.131:8888/api/private/v1/users",
        "params": {
            "pageNum": 1, "pageSize": 1
        },
        "data":None,
        "json": None,
        "files": None,
        "headers": None
    }
]
class TestRunner:
    @pytest.mark.parametrize("case", data)
    def test_case(self,case):
        res=requests.request(**case)
        print(res.json())
    # def test_login(self):
    #     assert True