import requests
import json
import time
from PIL import Image
import re


def get_ip():
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
    res = requests.get(url, headers=headers)
    # print(res.text)
    text = res.url
    ip_loc_list = [i.start() for i in re.finditer('ip=', text)]
    and_loc = text.find('&')
    wlanuserip = text[ip_loc_list[0] + 3:and_loc]
    basip = text[ip_loc_list[1] + 3:]
    return wlanuserip, basip


def get_captcha():
    current_time = int(time.time() * 1000)
    captcha_url = 'http://114.247.41.55/bjps/login/captcha.html?t=%d' % (current_time)
    r = requests.Session()
    ss = r.get(captcha_url)
    JSESSIONID = ss.cookies['JSESSIONID']
    route = ss.cookies['route']
    with open("captcha.BMP", "wb") as f:
        f.write(ss.content)
    im = Image.open('captcha.BMP')
    im.show()
    captcha = input('请输入验证码： ')
    return captcha, JSESSIONID, route


def verify(wlanuserip, basip, captcha, JSESSIONID, route):
    with open("config.txt", 'r') as load_f:
        line = load_f.readline()
        load_dict = json.loads(line)
    username = load_dict['username']
    password = load_dict['password']
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
        "Cookie": "JSESSIONID=%s; route=%s; base=%s; on=0; basip=%s; wlan=%s; wlanuserip=%s" % (
            JSESSIONID, route, basip, basip, wlanuserip, wlanuserip),
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A",
    }
    res = requests.post(url, data=data, headers=headers).text
    print(res)


if __name__ == '__main__':
    wlanuserip, basip = get_ip()
    print('获取ip成功！WlanUserIp为：%s，BasIp为：%s' % (wlanuserip, basip))
    captcha, JSESSIONID, route = get_captcha()
    print('获取验证码成功！captcha为：%s，JSessionID为：%s，route为：%s' % (captcha, JSESSIONID, route))
    verify(wlanuserip, basip, captcha, JSESSIONID, route)
