# -*- coding: utf-8 -*-

# pip install wxpy
# pip install requests

from __future__ import unicode_literals
from threading import Timer
from wxpy import *
import requests

#这里的二维码是用像素的形式打印出来，如果在Windows环境上运行，使用 bot=Bot() 就可以了
# bot = Bot(console_qr=2,cache_path="botoo.pkl")
bot = Bot()

def get_news1():
    #获取金山词霸每日一句，英文和翻译
    url = "http://open.iciba.com/dsapi/"
    r = requests.get(url)
    contents = r.json()['content']
    translation= r.json()['translation']
    return contents,translation
    # print(translation)

def send_news():
    try:
        my_friend = bot.friends().search(u'作数')[0]#朋友的微信昵称，不是备注，也不是微信帐号。
        my_friend.send(get_news1()[0])
        my_friend.send(get_news1()[1][5:])
        t = Timer(86400, send_news)#每86400秒（1天），发送1次，
        #不用linux的定时任务是因为每次登陆都需要扫描二维码登陆
        my_friend.send(u"来自爸爸的心灵鸡汤！")
        t.start()
    except:
        myself = bot.friends().search('月尚')[0]#自己的微信昵称，不是微信帐号。
        myself.send(u"今天消息发送失败了")
        
if __name__ == "__main__":
    send_news()
    # get_news1()