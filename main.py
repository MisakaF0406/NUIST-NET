import requests
import time
import os
import base64
t=os.path.isfile("D:/config1.txt")
if t==False:
    print("南京信息工程大学校园网认证自动化程序")
    print("Producted by 南京信息工程大学-程逸飞")
    print("检测到你是首次运行，即将开始配置！")
    print("注意：请确认已关闭所有杀毒软件！")
    print("若你的电脑没有D盘，则暂时无法使用本程序，请等待后续更新")
    print("BUG提交：42724758@qq.com")
    fo = open("D:/config.txt", "wt")
    u=input("请输入用户名:")
    d=input("请选择运营商:\n移动输入：CMCC  电信输入：ChinaNet  联通输入：Unicom\n请注意大小写:")
    p=input("请输入密码:")
    p=base64.b64encode(p.encode('utf-8'))
    p=str(p,'utf-8')
    fo.write(u+"\n")
    fo.write(d+"\n")
    fo.write(p+"\n")
    fo.close()
    fo = open("D:/config1.txt", "wt")
    fo.close()
    url = "http://a.nuist.edu.cn/index.php/index/login"
    data = {"username": u, "domain": d, "password": p}
    res = requests.post(url=url, data=data)
    print(res.text)
    print("3s后自动退出")
    time.sleep(3)
elif t==True:
    print("非首次运行，开始登录")
    text=[1,1,1]
    m=0
    f=open("D:/config.txt")
    lines=f.readlines()
    for line in lines:
        text[m]=line.strip()
        m=m+1
    f.close()
    print(text[0])
    print(text[1])
    print(text[2])
    url = "http://a.nuist.edu.cn/index.php/index/login"
    data = {"username":text[0],"domain":text[1],"password":text[2]}
    res = requests.post(url=url,data=data)
    print(res.text)
    print("3s后自动退出")
    time.sleep(3)
