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
    schedule.every().day.at("15:35").do(drinkingtea)
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
        requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(gids[i],"群发测试"))
        i+=1
    return

def drinkingtea():#喝茶
    global gids
    i=0
    if len(gids)==0:
        requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(123456,"gids.txt文件错误"))
        
    while i<len(gids):
        requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(gids[i],"三点几了，饮茶先啦。这是卡尔，卡尔知道你工作了一天非常辛苦，他給你递了一杯茶。说：谢谢卡尔"))
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
        requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(gids[i],"群发测试"))
        i+=1
    return
    
    
def nighty():#晚安
    global gids
    i=0
    if len(gids)==0:
        requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(123456,"gids.txt文件错误"))
        
    while i<len(gids):
        requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(gids[i],"群发测试"))
        i+=1
    return