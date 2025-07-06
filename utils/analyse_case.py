import logging
import allure

from config.config import BASE_URL


# behavior内的执行-测试步骤
@allure.step("解析请求参数")
def analyse_case(case):
    method = case['method']
    url = (BASE_URL + case['path'])
    # eval()函数必须传入字符串，故使用isinstance()用于判断数据是否为字符串
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
    logging.info(f"1.解析请求数据，结果为{requests_data}")
    return requests_data
