from user_db_api import DataBaseConnector
import json

ip_info = json.load(open("./ip_info.json", 'r', encoding='utf8'))
db = DataBaseConnector(ip_info.get("Redis"))


# 鎖定 大蒜、香菜、枸杞、