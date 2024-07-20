import unittest
from htmltestreport import HTMLTestReport

from config import BASE_DIR

suite=unittest.TestLoader().discover("./","test_Demo1.py")
runner=HTMLTestReport(BASE_DIR+"/report/login_test.html")
runner.run(suite)

