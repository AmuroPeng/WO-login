# 破解联通沃校园终端限制
##  2018年7月17日联通更新后到目前都可以用
# 环境
Windows，Mac  
将路由器的DHCP功能开启  
不要使用或后台运行联通提供的客户端  
如果宿舍断网，请在每天通电后重启路由器  
能够自动弹出联通网关登录界面即可正常使用
# 使用
1. 修改文件夹中config.txt双击打开，把账号密码按照写好的格式改为自己的  
2. 在文件夹中找到WO-login.exe并双击，等待输入验证码提示后，将验证码输入到命令行中，并点击回车

（单文件版本大约250M左右，主要是因为加入了自动打开图片预览功能多占用了240M左右的空间）
# 原理
![联通网关](https://github.com/AmuroPeng/WO-login/blob/master/img/wo.png)  
在HttpHeader中的User-Agent使用Mac Safari的标识（Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A）来登录
# 参考
https://www.cnblogs.com/A-FM/p/6802535.html
# 免责声明
仅限于于学术交流，请于下载24小时后删除。产生的一切后果与本人无关，一切责任由您自己承担。