from flask import Flask, request
from gevent.pywsgi import WSGIServer
import requests
import threading
import api
import timeapi

app = Flask(__name__)
'''监听端口，获取QQ信息'''
#@app.route('/')
#@app.route('/', methods=["POST"])
@app.route('/', methods=['GET','POST'])
def post_data():
    #if request.method == 'GET':
    if request.method == 'POST':
        if request.get_json().get('message_type')=='private':# 如果是私聊信息
            sender=gid = request.get_json().get('sender')#获取名字
            uid = request.get_json().get('sender').get('user_id') # 获取信息发送者的QQ号码
            message = request.get_json().get('raw_message') # 获取原始信息
            api.keyword(sender,message, uid) # 将 Q号和原始信息传到我们的后台
        if request.get_json().get('message_type')=='group':# 如果是群聊信息
            sender=gid = request.get_json().get('sender')#获取名字
            gid = request.get_json().get('group_id') # 获取群号
            uid = request.get_json().get('sender').get('user_id') # 获取信息发送者的QQ号码
            message = request.get_json().get('raw_message') # 获取原始信息
            api.keyword(sender,message, uid, gid) # 将 Q号和原始信息传到我们的后台
    return ""

def apprun():
    app.run(debug=False,threaded=True, host='127.0.0.1', port=5701)

if __name__ == '__main__':
    print('main runned')
    thread1 = threading.Thread(target=apprun)
    thread2 = threading.Thread(target=timeapi.myclock)
    #requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(123,"初始化1"))
    #app.run(debug=True, host='127.0.0.1', port=5701)
    thread1.start()
    thread2.start()
    #requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(123,"初始化2"))
    '''下面的方法不会reboot，但是届不到上报数据，暂时废弃'''
    #http_server=WSGIServer(('',5701),app)
    #http_server.serve_forever()