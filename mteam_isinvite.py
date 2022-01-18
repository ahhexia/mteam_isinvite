from wxpusher import WxPusher
import requests
from bs4 import BeautifulSoup
import time
from sys import exit


def send_messge():
    res = WxPusher.send_message(
        content = "m-team开放注册，请尽快注册",
        uids=[''], # 发送的微信uuid
        # topic_ids = "",
        token="" # wxpusher的apptoken
    )

    # print(res,type(res))
    if res["code"] == 1000:
        print("send to wechat success!")
    else:
        print("sending failed!")
        print(str(res))

def req_mteam():
    r = requests.get(r"https://bbs.m-team.cc/index.php?/forum/5-%E7%AB%99%E9%BB%9E%E6%B4%BB%E5%8B%95/")
    # print(r.text)

    soup = BeautifulSoup(r.text, "lxml") # 转成bs4
    result = soup.find_all("span", class_ = "ipsType_break ipsContained") # 找出所有文章
    frist_topic = result[0] # 第一个文章

    a_all = frist_topic.select("a") # 搜索其中a标签

    frist_a = a_all[0]  # 第一个a标签

    topic_title = frist_a["title"]
    # print(topic_title,len(topic_title),type(topic_title))
    # print(topic_title == "MT 搶注活動開放 Round 28 ")
    return topic_title

def main():

    while True:
        time.sleep(3600)
        result = req_mteam()
        if result == "MT 搶注活動開放 Round 28 ":
            print("未开放注册!")
        else:
            send_messge() # 推送微信消息
            exit() # 退出

if __name__ == "__main__":
    main()