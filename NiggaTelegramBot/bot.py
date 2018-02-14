#!/usr/bin/env python
# -*- coding: utf-8 -*-
import string
import telepot
from pprint import pprint
import time
from telepot.loop import MessageLoop
from datetime import datetime
from pytz import timezone
from getlink import *
# me kiep, py3 bat them dau .truoc file
# start script service startup
# sudo systemctl start myscript.service


news_arr=news2_arr=[]

token="498721541:AAHd_9T23zJw7IwaUkrZd7FmoVkHQmE8ZLQ"

#GET VN TIME UTC+7
def get_VN_Time(mode):
    zone = 'Asia/Ho_Chi_Minh'
    now_time = datetime.now(timezone(zone))

    fmt=''
    if mode=='d':
        fmt = "%d-%m-%y"
        return now_time.strftime(fmt)
    elif mode=='t':
        fmt= "%H:%M"
        t=now_time.strftime(fmt).split(':')
        t=[t[0],t[1]]
    return t


chat_BOT_id                     ="-1001304130077"       # BOT ID
chat_PREMIUM_CHANNEL_id         ="-1001306859591"       # MY PREMIUM CHANNEL
chat_PREMIUM_UK_CHANNEL_id      ="-1001174105918"       # MY PREMIUM UK CHANNEL
chat_PREMIUM_CHANNEL_buy_id     ="-1001322925605"       # CHANNEL BUY

chat_FREE_CHANNEL_id            ="@leaksign"            # MY FREE CHANNEL
chat_VIP_CHANNEL_id             ="-1001284723474"       # MY VIP CHANNEL


count_PREMIUM_CHANNEL=count_PREMIUM_UK_CHANNEL=count_VIP_CHANNEL=count_FREE_CHANNEL=0
list_channel=[chat_PREMIUM_CHANNEL_id,chat_PREMIUM_UK_CHANNEL_id,chat_VIP_CHANNEL_id,chat_FREE_CHANNEL_id]


bot= telepot.Bot(token=token)
#----------------------------------------- NEWS
news()
print (news_arr)

debug=False
f = open("log.txt", 'wb')
count_				=0
count_news			=0


def broadcast_NEWS(msg):
    bot.sendMessage(chat_id=chat_FREE_CHANNEL_id, text=msg)
#bot.sendMessage(chat_id=chat_BOT_id, text=msg)
    bot.sendMessage(chat_id=chat_BOT_id, text="[OK] BROADCAST NEWS")


def get_NEWS():
    news2_arr=news()
    for i in news2_arr:
        if i not in news_arr:
            print(news_arr)
            news_arr.append(i)
            broadcast_NEWS(i)


def broadcast_NEWDATE(msg):

    if(msg=="NEWDATE"):
        m="--------------------------"+str(today)
        for i in list_channel:
            bot.sendMessage(chat_id=i, text=m)
        print ("[OK]"+m)
        f.write('new date'+m)


    # BROADCAST SIGNALS FROM [PREMIUM BUY] CHANNEL TO [ALL CHANNEL]
def broadcast_msg(m):
    global count_
    m = m.upper()
    for i in list_channel:
        if i == chat_PREMIUM_CHANNEL_id or i == chat_PREMIUM_UK_CHANNEL_id:
            bot.sendMessage(chat_id=i, text=m)
            print ("[OK] SEND PREMIUM & PREMIUM UK CHANNEL")
        elif i == chat_VIP_CHANNEL_id:
            if count_ < 5:
                print ("[OK] SEND VIP CHANNEL")
                bot.sendMessage(chat_id=i, text=m)
            elif i == chat_FREE_CHANNEL_id:
                if count_ < 1:
                    print ("[OK] SEND FREE CHANNEL")
#pass
                    bot.sendMessage(chat_id=i, text=m)
    print ("[OK] Broadcast " + m)
    count_ = count_ + 1
    print ("Count",count_)
    f.write("NEW SIGNALS\n" + m.encode('utf-8'))


#BROADCAST ALL CHANNEL
def broadcast_test(msg):
    if(msg=="TEST"):
        m=""
        id_chat=0
        for i in list_channel:
            if i==chat_PREMIUM_CHANNEL_id:
                id_chat=i
                m=" PREMIUM TEST"
            if i==chat_PREMIUM_UK_CHANNEL_id:
                id_chat = i
                m=" PREMIUM UK TEST"
            if i==chat_VIP_CHANNEL_id:
                id_chat = i
                m=" VIP TEST"
            if i==chat_FREE_CHANNEL_id:
                id_chat = i
                m=" FREE TEST"

            bot.sendMessage(chat_id=id_chat, text=m)
        print ("[OK] Broadcast "+m)
        f.write("TEST BROADCAST")
    elif msg=="NEWDATE":
        broadcast_NEWDATE(msg)
    elif msg=="NEWS":
        get_NEWS()
    else:
        msg=msg.lower()
        if ("coin name" in msg or "coin" in msg) and ("buy" in msg or "sell" in msg):
            msg=msg.upper()
            broadcast_msg(msg)
            print ("[OK] SEND MANUAL SIGNALS")
            f.write("SEND MANUAL SIGNALS\n"+msg.encode('utf-8'))


def process(m):
    mm=m.strip()
    mm=mm.lower()
    #print mm
    if ("coin name" in mm or "coin" in mm) and ("buy" in mm or "sell" in mm):
        broadcast_msg(mm)
        print ("[OK] SEND SIGNALS")
    else:
        print  ("NOT OK")

def handle(msg):
    m = msg['text']
    if debug:
        print (msg)
    #BROADCAST SIGNALS TO ALL CHANNEL
    if msg['chat']['id']==int(chat_PREMIUM_CHANNEL_buy_id):
        print ("[RECV] New SIGNALS")
        process(m)
    #TEST ALL CHANNEL
    elif msg['chat']['id']==int(chat_BOT_id):
        print ("[RECV] TEST")
        broadcast_test(m)



if __name__=='__main__':
    today2=today = get_VN_Time('d')
    print ("Today:",today)


    bot.message_loop(handle)
while 1:
    today2 = get_VN_Time('d')
    new_time=get_VN_Time('t')
    #print int(new_time[0]),int(new_time[1])
    if (today != today2):
        count = 0
        print ("New date", today2)
        print ("count", count)
        broadcast_NEWDATE("NEWDATE")
        today=today2
        f.write("NEWDATE: " + today+"\n\n")
        f.close()
        f = open("log.txt", 'wb')
#print int(new_time[0]),int(new_time[1])
    else:
        if int(new_time[0])==6 and (int(new_time[1])==0   or int(new_time[1])==1):
            news2_arr=news()
            print (new_time)
            get_NEWS()
        elif int(new_time[0])==11 and (int(new_time[1])==0 or int(new_time[1])==1):
            news2_arr=news()
            print (new_time)
            get_NEWS()
        elif int(new_time[0])==18 and (int(new_time[1])==0 or int(new_time[1])==1):
            news2_arr=news()
            print (new_time)
            get_NEWS()
    time.sleep(10)