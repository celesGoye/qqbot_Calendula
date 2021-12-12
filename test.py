import threading
import schedule
import time
import datetime
 
import os
path = os.getcwd()

def job():
    print("working")
    return

'''print("hello")
schedule.every().day.at("14:34").do(job)
while True:
    schedule.run_pending()
    time.sleep(1)'''

f=open(path+r".\userdata\gids.txt","r")
for x in f:
    x = x.strip('\n')
    print(x)

f.close()