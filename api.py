import json
import time
import datetime
import requests
import re
import random
import os
path = os.getcwd()

def keyword(sender,message, uid, gid = None):
    if message[0:2]=='hi':
        helloworld(uid,gid,sender)
    if message[0:2] == '.r': 
        rollingdice(uid,gid,sender,message)
    if message[0:3]=='吃什么':
        whattoeat(uid,gid,sender)
    if message[0:5]=='石头剪刀布' or message[0:5]=='剪刀石头布':
        rockpaperscissors(uid,gid,sender)
    if message[0:2] == '晚安': 
        nighty(uid,gid,sender)
    if message[0:2] == '狗图': 
        cutedog(uid,gid)
    if message[0:3] == '拼动物':
        animals(uid,gid)
    if message[0:3] == '卡尔，': 
        whichone(uid,gid,message)
    #if message[0:4] == 'setu': # 你们懂的
    #    setu()
    
    
#连接测试
def helloworld(uid,gid,sender):
    if gid != None: # 如果是群聊信息
        sendername=list(sender.values())[2] if list(sender.values())[2]!="" else list(sender.values())[4]
        requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1} '.format(gid,'卡尔说 Hello World!'+sendername))
    else: # 如果是私聊信息
        requests.get(url='http://127.0.0.1:5700/send_private_msg?user_id={0}&message={1}'.format(uid, '卡尔说Hello World!'+list(sender.values())[1]))
#-------------------------
#骰娘
def rollingdice(uid,gid,sender,message):
    str_rollingdice=""
    str_diceface=""
    i=2
    if message=='r.':
        str_rollingdice="1"
        str_diceface="100"
        r=mydice(1,100)
    else: 
        while i<len(message):
            if bool(1-isnumber(message[i])):
                break
            str_rollingdice=str_rollingdice+message[i]
            i+=1
        
        if message[i]=='d' and (i+1<len(message)):
            i+=1
            while i<len(message):
                if bool(1-isnumber(message[i])):
                    break
                str_diceface=str_diceface+message[i]
                i+=1
            if bool(1-isnumber(str_diceface)) or bool(1-isnumber(str_rollingdice)):
                r=-1
            else:
                r=mydice(int(str_rollingdice),int(str_diceface))
        else:
            r=-1
                
    if gid != None: # 如果是群聊信息
        sendername=list(sender.values())[2] if list(sender.values())[2]!="" else list(sender.values())[4]
        if r<0:
            requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(gid,"卡尔说"+sendername+"的参数好像有问题"))
        else:
            requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(gid,"卡尔说"+sendername+"投出了"+str(r)+mydicecmt(int(str_rollingdice),int(str_diceface),r)))
    else: # 如果是私聊信息
        if r<0:
            requests.get(url='http://127.0.0.1:5700/send_private_msg?user_id={0}&message={1}'.format(uid,"卡尔说"+list(sender.values())[1]+"的参数好像有问题"))
        else:
            requests.get(url='http://127.0.0.1:5700/send_private_msg?user_id={0}&message={1}'.format(uid,"卡尔说"+list(sender.values())[1]+"投出了"+str(r)+mydicecmt(int(str_rollingdice),int(str_diceface),r)))

def isnumber(mystr):
    try:
        float(mystr)
        return True
    except ValueError:
        pass
    return False

def mydice(t,num):
    if t<=0:
        return -1
    result=0
    i=0
    while i<t:
        result+=random.randint(1,num)
        i+=1
    return result

def mydicecmt(t,num,r):
    if num==100 and t==1:
        if r==1:
            return "，超级超级稀有的大成功！"
        if r>1 and r<=20:
            return "，超级厉害的极难成功！"
        if r>20 and r<=50:
            return "，困难成功！"
        else:
            return "，问题不大"
    else:
        return ""
#-------------------------
#吃什么
def whattoeat(uid,gid,sender):
    if gid != None: # 如果是群聊信息
        sendername=list(sender.values())[2] if list(sender.values())[2]!="" else list(sender.values())[4]
        requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(gid,"卡尔说"+sendername+"要不要吃"+rollingmeal()))
    else: # 如果是私聊信息
        requests.get(url='http://127.0.0.1:5700/send_private_msg?user_id={0}&message={1}'.format(uid,"卡尔说"+ list(sender.values())[1]+"要不要吃"+rollingmeal()))

def rollingmeal():
    meals=("社畜快餐","汉堡","米粉米线","粥","四川风味","麻辣烫","香锅","炸鸡","烤串","陕西风味","长沙风味","日式定食","羊肉汤","港餐","便利店","猪脚饭","北方火锅","南方火锅","烤鱼","酸菜鱼","牛杂","拉面","肠粉","螺狮粉","椰子鸡","狂乱木曜日","鸡公煲","炒饭","烤内脏","烤鸡","烤鸭","烧鹅","麦辣鸡翅","提拉米苏","咖喱","萨莉亚","东南亚菜","情寻糯米叉烧包")
    return meals[random.randint(0,len(meals)-1)]
#-------------------------
#石头剪刀布
def rockpaperscissors(uid,gid,sender):
    if gid != None: # 如果是群聊信息
        sendername=list(sender.values())[2] if list(sender.values())[2]!="" else list(sender.values())[4]
        requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(gid,"卡尔说"+sendername+"使出了"+rollingrock()))
    else: # 如果是私聊信息
        requests.get(url='http://127.0.0.1:5700/send_private_msg?user_id={0}&message={1}'.format(uid,"卡尔说"+ list(sender.values())[1]+"使出了"+rollingrock()))
    
def rollingrock():
    skills=("石头","剪刀","布")
    return skills[random.randint(0,3)]
#-------------------------
#晚安
def nighty(uid,gid,sender):
    if gid != None: # 如果是群聊信息
        sendername=list(sender.values())[2] if list(sender.values())[2]!="" else list(sender.values())[4]
        requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(gid,"卡尔向"+sendername+"说晚安,卡尔希望你一夜好梦[CQ:image,file=http://gchat.qpic.cn/gchatpic_new/0/530077417-0-FFBD8609C6837A1F812B905F0510A18A/0]&auto_escape=false"))
    else: # 如果是私聊信息
        requests.get(url='http://127.0.0.1:5700/send_private_msg?user_id={0}&message={1}'.format(uid,"卡尔向"+list(sender.values())[1]+"说晚安[CQ:image,file=http://gchat.qpic.cn/gchatpic_new/0/530077417-0-FFBD8609C6837A1F812B905F0510A18A/0]&auto_escape=false"))

#-------------------------
#拼动物
def animals(uid,gid):
    if gid != None: # 如果是群聊信息
        requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(gid,getanimal()+"  X  "+getanimal()))
    else: # 如果是私聊信息
        requests.get(url='http://127.0.0.1:5700/send_private_msg?user_id={0}&message={1}'.format(uid,getanimal()+"  X  "+getanimal()))
        
def getanimal():
    f=open(path+r"\..\texts\animals.txt","r",encoding='utf-8')
    animalname=f.readlines()
    randomnum=random.randint(0,len(animalname)-1)
    return animalname[randomnum]
#-------------------------
#狗图        
def cutedog(uid,gid):
    if gid != None: # 如果是群聊信息
        requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(gid,"[CQ:image,file="+getcutedogurl()+"]&auto_escape=false"))
    else: # 如果是私聊信息
        requests.get(url='http://127.0.0.1:5700/send_private_msg?user_id={0}&message={1}'.format(uid,"[CQ:image,file="+getcutedogurl()+"]&auto_escape=false"))
        
def getcutedogurl():
    f=open(path+r"\..\images\cutedog.txt","r")
    urls=f.readlines()
    return urls[random.randint(0,len(urls)-1)].replace('\n', '')
#-------------------------
#二选一
def whichone(uid,gid,message):
    str_first=""
    str_second=""
    i=3
    if message=="卡尔，":
        return
    else: 
        while i<len(message):
            if i+1==len(message):
                return
            if bool(message[i]+message[i+1]=="还是"):#检测还是
                if i==3:                            #还是前为空？ 
                    return
                break
            str_first=str_first+message[i]          #first
            i+=1   
        if message[i]+message[i+1]=="还是" and (i+1<len(message)):
            i+=2
            while i<len(message):
                str_second=str_second+message[i]    #second
                i+=1
        else:
            return
        result=str_first if random.randint(0,1) else str_second
    if gid != None: # 如果是群聊信息
        requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(gid,"卡尔说"+result))
    else: # 如果是私聊信息
        requests.get(url='http://127.0.0.1:5700/send_private_msg?user_id={0}&message={1}'.format(uid,"卡尔说"+result))
"""def setu(): 
    '本功能放在下面讲，这里的功能默认只有群聊，没考虑私聊，请把机器人拉进群再发消息'
    '如果想实现私聊功能可以参考上面查战绩的代码'
    key = ''
    url = 'https://api.lolicon.app/setu?apikey=' + key + r'&size1200=true'
    menu = requests.get(url)
    setu_url = menu.json()['data'][0]['url'] # 对传回来的涩图网址进行数据提取
    requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(gid, r'[CQ:image,' r'file=' + str(setu_url) + r']'))"""