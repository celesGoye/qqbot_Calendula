import json
import time
import datetime
import requests
import re
import random
import threading
import schedule
import os
path = os.getcwd()

global gids
gids=[]

def myclock():
    global gids
    f=open(path+r".\userdata\gids.txt","r")
    i=0
    for x in f:
        x = x.strip('\n')
        gids.append(x)

    f.close()
    
    schedule.every().day.at("07:00").do(morning)
    schedule.every().day.at("07:05").do(cutedog)
    schedule.every().day.at("10:00").do(drinkingwater)
    schedule.every().day.at("15:38").do(drinkingtea)
    schedule.every().day.at("14:30").do(drinkingwater)
    schedule.every().day.at("23:59").do(nighty)
    #schedule.every(10).seconds.do(drinkingtea)
    while True:
        schedule.run_pending()
        time.sleep(60)
    

def drinkingcoco():#喝可可
    global gids
    i=0
    if len(gids)==0:
        requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(123456,"gids.txt文件错误"))
        
    while i<len(gids):
        requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(gids[i],"群发测试"))
        i+=1
    return

def drinkingwater():#喝水
    global gids
    i=0
    if len(gids)==0:
        requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(123456,"gids.txt文件错误"))
        
    while i<len(gids):
        requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(gids[i],"这是卡尔，卡尔给你带了一杯水。卡尔希望你无论如何都一定要保持水分[CQ:image,file=http://gchat.qpic.cn/gchatpic_new/0/530077417-0-5B8F3E7B90ADB949459C8AE0064694A0/0]&auto_escape=false"))
        i+=1
    return

def drinkingtea():#喝茶
    global gids
    i=0
    if len(gids)==0:
        requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(123456,"gids.txt文件错误"))
        
    while i<len(gids):
        requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(gids[i],"三点几了，饮茶先啦。这是卡尔，卡尔给你准备了下午茶。卡尔知道你工作了一天非常辛苦，休息一下喝口茶，说：谢谢卡尔[CQ:image,file=http://gchat.qpic.cn/gchatpic_new/0/530077417-0-562DAE4EF363886BB016F738B50C803E/0]&auto_escape=false"))
        i+=1
    return
   

def havearest():#休息
    global gids
    i=0
    if len(gids)==0:
        requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(123456,"gids.txt文件错误"))
        
    while i<len(gids):
        requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(gids[i],"群发测试"))
        i+=1
    return
    
def morning():#早安
    global gids
    i=0
    if len(gids)==0:
        requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(123456,"gids.txt文件错误"))
        
    while i<len(gids):
        requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(gids[i],"这是卡尔，卡尔给你准备了早餐，希望你的今天也是顺利的一天。说：谢谢卡尔[CQ:image,file=http://gchat.qpic.cn/gchatpic_new/0/530077417-0-141A9CB98CB87056084699C152C0C1C4/0]&auto_escape=false"))
        i+=1
    return
    
    
def nighty():#晚安
    global gids
    i=0
    if len(gids)==0:
        requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(123456,"gids.txt文件错误"))
        
    while i<len(gids):
        requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(gids[i],"这是卡尔，卡尔决定在十二点钟之前睡觉，过医生都说我很健康的生活，学学卡尔。[CQ:image,file=http://gchat.qpic.cn/gchatpic_new/0/530077417-0-319D73754DC847734406C0E253E72C68/0]&auto_escape=false"))
        i+=1
    return

def cutedog():
    global gids
    i=0
    if len(gids)==0:
        requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(123456,"gids.txt文件错误"))
        
    while i<len(gids):
        requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(gids[i],"卡尔给你带来了今日的晨间狗图[CQ:image,file="+getcutedogurl()+"]&auto_escape=false"))
        i+=1
    return
        
def getcutedogurl():
    f=open(path+r"\..\images\cutedog.txt","r")
    urls=f.readlines()
    return urls[random.randint(0,len(urls)-1)].replace('\n', '')