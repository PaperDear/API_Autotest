import jsonpath
import pymysql
import pytest
import requests
from jinja2 import Template

from utils.excel_utils import read_excel


class TestRunner:
    # 读取测试数据-->dict
    data = read_excel()
    # 空字典用于提取全局变量
    all = {}
    @pytest.mark.parametrize("case", data)
    def test_case(self, case):
        # 获取到全局变量后使用jinja2渲染模板，将请求头中需要的token通过渲染带入
        # dict类型在操作template需要先强制转换为str，再通过render()进行渲染
        # 在使用case时需要是dict，所以通过eval再转换回去
        case = eval(Template(str(case)).render(self.all))
        # 1.提取请求参数
        method = case['method']
        url = 'http://192.168.10.131:8888/api/private/v1' + case['path']
        # eval()函数可将字符串当做Python的表达式执行并返回-->将字符串转成对应数据类型
        # num=eval('42'),type(num)为int
        # 因为eval()函数必须传入字符串，故使用isinstance()用于判断数据是否为字符串
        data = eval(case['data']) if isinstance(case['data'], str) else None
        params = eval(case['params']) if isinstance(case['params'], str) else None
        json = eval(case['json']) if isinstance(case['json'], str) else None
        files = eval(case['files']) if isinstance(case['files'], str) else None
        headers = eval(case['headers']) if isinstance(case['headers'], str) else None
        requests_data = {
            'method': method,
            'url': url,
            'data': data,
            'params': params,
            'json': json,
            'files': files,
            'headers': headers
        }
        # 2.发送请求
        res = requests.request(**requests_data)
        print(res.json())

        # 3.断言
        # HTTP响应断言
        if case['check']:
            # 可以直接提取到的值可以直接判断预期结果
            # jsonpath()返回的是一个列表，需要取列表值
            assert jsonpath.jsonpath(res.json(), case['check'])[0] == case['expected']
        else:
            # 不好直接提取的值可以判断是否在响应文本中
            # case获取到的是字符串，不能判断是否在字典res.json()中
            assert case['expected'] in res.text

        # 数据库断言
        if (case['sql_check'] and case['sql_expected']):
            # 连接数据库
            conn = pymysql.connect(
                host='192.168.10.131',
                user='root',
                password='123456',
                database='mydb',
                port=3306,
                charset='utf8'
            )
            # 做个游标
            cursor = conn.cursor()
            # 执行sql语句
            cursor.execute(case['sql_check'])
            # fetchone()返回的是元组
            result = cursor.fetchone()
            # 关闭资源
            cursor.close()
            conn.close()
            # 断言的时候需要取元组值
            assert result[0] == case['sql_expected']

        # 4.提取参数
        # JSON提取
        if case['jsonExData']:
            # case['jsonExdata']提取到的是字符串，需要转为字典类型
            for key, value in eval(case['jsonExData']).items():
                value = jsonpath.jsonpath(res.json(), value)[0]
                # all在TestRunner类中，需要self进行引用
                self.all[key] = value
        # 数据库提取
        if case['sqlExData']:
            conn = pymysql.connect(
                host='192.168.10.131',
                user='root',
                password='123456',
                database='mydb',
                port=3306,
                charset='utf8'
            )
            cursor = conn.cursor()
            for key, value in eval(case['sqlExData']).items():
                cursor.execute(value)
                value = cursor.fetchone()
                self.all[key] = value[0]
            cursor.close()
            conn.close()
