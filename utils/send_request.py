import logging
import allure
import requests, pymysql

from config.config import *


@allure.step("发送http请求")
def send_http_request(**requests_data):
    res = requests.request(**requests_data)
    logging.info(f"2.发送http请求，响应结果为:{res.text}")
    allure.attach(f'{res.text}', "http响应结果")
    return res


@allure.step("发送数据库连接请求-查询")
def send_jdbc_request(sql, index=0):
    conn = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_DATABASE,
        port=DB_PORT,
        charset=DB_CHARSET
    )
    # 建立游标
    cursor = conn.cursor()
    # 执行sql语句
    cursor.execute(sql)
    # fetchone/all()返回的是tuple，需要取结果时给对应index
    result = cursor.fetchone()
    # 关闭资源
    cursor.close()
    conn.close()
    return result[index]


@allure.step("发送数据库连接请求-增删改")
def sql_execute(sqls, index=0):
    conn = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_DATABASE,
        port=DB_PORT,
        charset=DB_CHARSET,
        autocommit=True
    )
    # 建立游标
    cursor = conn.cursor()
    # 执行sql语句
    for sql in sqls:
        cursor.execute(sql)

    # 关闭资源
    cursor.close()
    conn.close()
