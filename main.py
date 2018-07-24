import requests
import json

# 验证
with open("config.json", 'r') as load_f:
    load_dict = json.load(load_f)
username = load_dict['username']
password = load_dict['password']
print(username, password)
JSESSIONID = '25F5CFF6D24500A324C5F69EF88035D7'
route = 'ede4c0529c7236acaea3c1a75d5ef384'
basip = '61.148.2.182'
wlanuserip = '172.16.17.139'
XK = 'U-CB51DE0BA39FC5F971B3947FC101437C'
captcha = ''

url = "http://114.247.41.55/bjps/login/online.html"
data = {
    "userName": username,
    "lpsPwd": password,
    "captcha": captcha,
    "wlanuserip": wlanuserip,
    "basip": basip,
}
headers = {
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": "JSESSIONID=%s; route=%s; base=%s; on=0; basip=%s; wlan=%s; wlanuserip=%s; XK=%s" % (
        JSESSIONID, route, basip, basip, wlanuserip, wlanuserip, XK),
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A",
}
print(headers['Cookie'])
res = requests.post(url, data=data, headers=headers).text
print(res)

if __name__ == '__main__':
    print(1)