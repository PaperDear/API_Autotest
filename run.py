import os

import pytest

if __name__ == '__main__':
    pytest.main(['-vs', './testcases/test_case.py',
                 '--alluredir=./report/json_report', '--clean-alluredir'])
    os.system(r"allure generate ./report/json_report -o ./report/html_report --clean")

