import redis
ip=

userid = 

user_refri_dict = {"高麗菜":"5,顆,2020/10/23",
                   "金針菇":"2,根,2020/10/23",
                   "蔥":"5,個,2020/10/24",
                   "羊肉":"7,個,2020/10/21",
                   "雞蛋":"3,個,2020/10/24",
                   "番茄":"10,顆,2020/10/24",
                   "豬肉":"200,gram,2020/10/19",
                   "太白粉":"500,gram,2020/10/01",
                   "麵粉":"500,gram,2020/10/01",
                   }

r = redis.StrictRedis(host=ip, port=6379, decode_responses=True)

r.hmset(userid, user_refri_dict)