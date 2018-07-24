import json
import requests

# new_dict = {'a':1,'b':2}
# with open("config.json","w") as f:
#      json.dump(new_dict,f)

# with open("config.json", 'r') as load_f:
#     load_dict = json.load(load_f)
#     print(load_dict['username'])
# url = 'http://114.247.41.55:80/bjps'
# url = 'www.baidu.com'
url = 'http://www.msftconnecttest.com/redirect'

headers = {
    # "Host": "www.msftconnecttest.com",
    # "Connection": 'Connection',
    "Upgrade-Insecure-Requests": '1',
    # "Accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    # "Accept-Encoding": 'gzip, deflate',
    # "Accept-Language": 'zh-CN,zh;q=0.9',
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A",
}
res = requests.get(url, headers=headers).text
print(res)