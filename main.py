import requests
import time
import getpass
import os
import shutil
import base64

t = os.path.isfile("C:/config1.txt")
name = getpass.getuser()  # 当前用户名
r1 = os.getcwd()  # 当前路径

if t == False:
    r2 = os.path.join(r1, "/main.exe")
    start = "C:/Users/" + name + "/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup"  # 开机自启动路径
    start1 = start + "/main.exe"
    # if os.path.exists(start+"/main.exe"):
    # os.remove(start+"/main.exe")
    print("南京信息工程大学校园网认证自动化程序")
    print("Producted by 南京信息工程大学-程逸飞")
    print("检测到你是首次运行，即将开始配置！")
    m = input("请选择是否使用i-NUIST，是则输1回车，不是则输0回车\n注意，对于有双网卡的笔记本，若你不使用i-NUIST，开机后可能会不自动连接wifi，导致登录失败\n")
    if m == "1":
        t3 = os.system("netsh wlan connect i-NUIST")
        if t3 == 0:
            print("网络配置成功，开始配置账户")
            fo = open("C:/config.txt", "wt")
            tt = "1"
            u = input("请输入用户名:")
            d = input("请选择运营商:\n移动输入：CMCC  电信输入：ChinaNet  联通输入：Unicom\n请注意大小写:")
            p = input("请输入密码:")
            p = base64.b64encode(p.encode('utf-8'))
            p = str(p, 'utf-8')
            fo.write(u + "\n")
            fo.write(d + "\n")
            fo.write(p + "\n")
            fo.write(tt +"\n")
            fo.close()
            fo = open("C:/config1.txt", "wt")
            fo.close()
            url = "http://a.nuist.edu.cn/index.php/index/login"
            data = {"username": u, "domain": d, "password": p}
            res = requests.post(url=url, data=data)
            print(res.text)
            print("配置完成，3s后自动退出")
            # os.system("copy r2 start")
            time.sleep(3)
        else:
            print("error")
    elif m == "0":
        fo = open("C:/config.txt", "wt")
        u = input("请输入用户名:")
        d = input("请选择运营商:\n移动输入：CMCC  电信输入：ChinaNet  联通输入：Unicom\n请注意大小写:")
        p = input("请输入密码:")
        p = base64.b64encode(p.encode('utf-8'))
        p = str(p, 'utf-8')
        fo.write(u + "\n")
        fo.write(d + "\n")
        fo.write(p + "\n")
        fo.close()
        fo = open("C:/config1.txt", "wt")
        fo.close()
        url = "http://a.nuist.edu.cn/index.php/index/login"
        data = {"username": u, "domain": d, "password": p}
        res = requests.post(url=url, data=data)
        print(res.text)
        print("3s后自动退出")
        # shutil.copy(r2, start)
        time.sleep(3)
elif t == True:
    print("非首次运行")
    text = [1, 1, 1, 0]
    m = 0
    f = open("C:/config.txt")
    lines = f.readlines()
    for line in lines:
        text[m] = line.strip()
        m = m + 1
        f.close()
    print(text[0])
    print(text[1])
    print(text[2])
    print(text[3])
    if text[3] == "1":
        os.system("netsh wlan connect i-NUIST")
        print("连接i-NUIST成功，开始登录")
        time.sleep(5)
        url = "http://a.nuist.edu.cn/index.php/index/login"
        data = {"username": text[0], "domain": text[1], "password": text[2]}
        res = requests.post(url=url, data=data)
        print(res.text)
        print("3s后自动退出")
        time.sleep(3)
    elif text[3] == "0":
        url = "http://a.nuist.edu.cn/index.php/index/login"
        data = {"username": text[0], "domain": text[1], "password": text[2]}
        res = requests.post(url=url, data=data)
        print(res.text)
        print("3s后自动退出")
        time.sleep(3)
