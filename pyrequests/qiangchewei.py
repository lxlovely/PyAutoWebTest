# !usr/bin/env python
# -*- coding:utf-8 _*-

import threading
import requests


SetHeader = '''
Host: ztcwx.myscrm.cn
Connection: keep-alive
Accept: */*
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Linux; Android 8.0; DUK-AL20 Build/HUAWEIDUK-AL20; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/044306 Mobile Safari/537.36 MicroMessenger/6.7.2.1340(0x2607023A) NetType/4G Language/zh_CN
Content-Type: application/x-www-form-urlencoded;charset=utf-8
Referer: https://ztcwx.myscrm.cn/page/room.html?token=sxshes1502248391&activityId=4701&chooseRoomId=2555313
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,en-US;q=0.8
Cookie: aliyungf_tc=AQAAAIb9VQaLUQEASh7Pi8mlsczyXAOS; PHPSESSID=4j3nkfpd9u7iahfo2prcmb3ac7; env_orgcode=cdhradmin; public_no_token=76c77294cac4da3eec7ba984bd05d09c5fd70929c7a43ccef3eee02fdffcdbeba%3A2%3A%7Bi%3A0%3Bs%3A15%3A%22public_no_token%22%3Bi%3A1%3Bs%3A16%3A%22sxshes1502248391%22%3B%7D; yunke_org_id=9b44d15cf528ab7dfef8609cc8c33667c1cf9b1bdfb900f358f18b82b022a49aa%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22yunke_org_id%22%3Bi%3A1%3Bs%3A36%3A%2239e0d6bf-0666-bcff-d45f-34309fd165cf%22%3B%7D; ztc_org_id=84e9c019a6312aa67f1d1b5ec307eae0999fb8322dd9ff671b46b820b103d751a%3A2%3A%7Bi%3A0%3Bs%3A10%3A%22ztc_org_id%22%3Bi%3A1%3Bi%3A508%3B%7D; _alicdn_sec__=5bcdf4c99684dcfc42ab817c4ca15a7287808af7; last_env=g2
'''


# 设置Header头信息
def CheckStr(Header):
    Headers = {}
    for i in Header.split("\n"):
        if i != None or i != "" or i != '':
            data = i.split("\n")
            if data[0] != None or data[0] != '' or data[0] != '\n':
                twodata = data[0].split(": ")
                try:
                    Headers[twodata[0]] = twodata[1]
                except:
                    pass
    return Headers


# 设置url查询数据
def SetData(token,chooseRoomId=2555313):
    urlquery = "r=choose-room/get-random-code&token=%s&chooseRoomId=%s&activityVersion=3"%(token,chooseRoomId)
    return urlquery


# 查询车位信息接口
# url = "https://ztcwx.myscrm.cn/index.php?r=choose-room/room&token=sxshes1502248391&chooseRoomId=2554797"

# 抢车位接口
def CheckCheWei(token,chooseRoomId,SetHeader):
    # 解决requests请求https时错误警告的问题
    requests.packages.urllib3.disable_warnings()

    # 定义Header信息
    url = "https://ztcwx.myscrm.cn/index.php?%s" % SetData(token, chooseRoomId)
    html = requests.get(url=url, headers=SetHeader, verify=False, timeout=100).text
    print(html)


# 添加线程组，添加QuicklyBuild文本文档中的文件
def AddThrad(token,chooseRoomId,SetHeader):
    Threads = []
    for i in range(100):
        Athread = threading.Thread(target=CheckCheWei, args=(token, chooseRoomId, SetHeader))
        Threads.append(Athread)
    return Threads

if __name__ == "__main__":

    # 选择车位接口
    token = "sxshes1502248391"

    SetHeader = CheckStr(SetHeader)
    chooseRoomId = [2555313, 2554806, 2555347]

    # 抢车位 B1-3312
    one = AddThrad(token,chooseRoomId[0],SetHeader)
    # 遍历执行线程组
    for t in one:
        t.setDaemon(True)
        t.start()
    t.join()

    # 抢车位 B3-3706
    two = AddThrad(token,chooseRoomId[1],SetHeader)
    # 遍历执行线程组
    for t in two:
        t.setDaemon(True)
        t.start()
    t.join()

    # 抢车位 B3-2788
    three = AddThrad(token,chooseRoomId[1],SetHeader)
    # 遍历执行线程组
    for t in three:
        t.setDaemon(True)
        t.start()
    t.join()