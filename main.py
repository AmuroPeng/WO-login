#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import json
import time
import re
import sys
# 1
from PIL import Image


#
# 2
# import matplotlib.pyplot as plt  # plt 用于显示图片
# import matplotlib.image as mpimg  # mpimg 用于读取图片
#


def get_ip():
    print('（1/4）尝试获取ip地址...')
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
    try:
        res = requests.get(url, headers=headers)
    except:
        get_error(1)
    text = res.url
    if text.find('msn') != -1:
        get_error(2)
    if text.find('wlanuserip') == -1:
        print('log：获取到的url为：' + text)
        get_error(3)
    ip_loc_list = [i.starjt() for i in re.finditer('ip=', text)]
    and_loc = text.find('&')
    wlanuserip = text[ip_loc_list[0] + 3:and_loc]
    basip = text[ip_loc_list[1] + 3:]
    return wlanuserip, basip


def get_captcha():
    print('（2/4）尝试获取验证码...')
    try:
        current_time = int(time.time() * 1000)
        captcha_url = 'http://114.247.41.55/bjps/login/captcha.html?t=%d' % (current_time)
        r = requests.Session()
        ss = r.get(captcha_url)
        print(1111111111111111111111111)
        print(ss.cookies)
        JSESSIONID = ss.cookies['JSESSIONID']
        route = ss.cookies['route']
    except:
        print('log：current_time:'+str(current_time)+' captcha_url:'+str(captcha_url)+' cookies:'+str(ss.cookies))
        get_error(4)
    #该这里的try了！！！
    with open("captcha.BMP", "wb") as f:
        f.write(ss.content)
    # 1
    im = Image.open('captcha.BMP')
    im.show()
    #
    # 2
    # lena = mpimg.imread('captcha.BMP')  # 读取和代码处于同一目录下的
    # plt.imshow(lena)  # 显示图片
    # plt.axis('off')  # 不显示坐标轴
    # plt.show()
    #
    captcha = input('请输入验证码： ')
    # readme里写下captcha.BMP的位置
    return captcha, JSESSIONID, route


def verify(wlanuserip, basip, captcha, JSESSIONID, route):
    print('（3/4）尝试进行登录...')
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


def get_error(num):
    error_title = str(sys.exc_info()[0])
    error_info = str(sys.exc_info())
    print('发现错误：' + error_title)
    print('具体信息：' + error_info)
    error_info = error_dict(num)
    input('#####错误' + str(num).rjust(3, '0') + '：' + error_info)
    sys.exit(0)


def error_dict(num):
    numbers = {
        0: "zero",
        1: "网络连接异常，检查网线是否插好/WiFi是否连接，请连接正常后重试。按回车键退出(ノ_<。)",
        2: "网络已经正常连接~ 无需再次登录,按回车键退出( •̀ ω •́ )y",
        3: "无法获取ip地址，请重启路由器/重新连接光猫后重试。按回车键退出(ノ_<。)",
        4: "获取验证码失败，请重启本程序再次尝试。按回车键退出(ノ_<。)"
    }
    return numbers.get(num, None)


if __name__ == '__main__':
    wlanuserip, basip = get_ip()
    print('获取ip成功！WlanUserIp为：%s，BasIp为：%s' % (wlanuserip, basip))
    captcha, JSESSIONID, route = get_captcha()
    print('获取验证码成功！captcha为：%s，JSessionID为：%s，route为：%s' % (captcha, JSESSIONID, route))
    verify(wlanuserip, basip, captcha, JSESSIONID, route)
