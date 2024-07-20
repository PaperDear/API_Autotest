import unittest

from case.test_Demo2 import TestDemo2
from config import BASE_DIR

suite = unittest.TestLoader().discover(BASE_DIR+'/case', 'test_Demo2.py')
unittest.TextTestRunner(verbosity=2).run(suite)



