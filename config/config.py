# 环境基准地址
BASE_URL="http://192.168.10.131:8888/api/private/v1"

# excel格式的用例文件配置
CASE_FILE="./data/cases.xlsx"
SHEET_NAME="Sheet1"

# MySQL配置
DB_HOST="192.168.10.131"
DB_USER="root"
DB_PASSWORD="123456"
DB_DATABASE="mydb"
DB_PORT=3306
DB_CHARSET="utf8"

# MySQL资源销毁
SQLS=["delete from sp_manager where mg_name='Jay'"]