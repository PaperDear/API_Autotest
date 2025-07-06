import pytest

from config.config import SQLS
from send_request import  sql_execute

@pytest.fixture(scope="session", autouse=True)
def destroy_data(sqls=SQLS):
    sql_execute(sqls)
