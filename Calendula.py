from flask import Flask, request
import api

#global counter
#counter=0
app = Flask(__name__)
'''监听端口，获取QQ信息'''
#@app.route('/')
#@app.route('/', methods=["POST"])
@app.route('/', methods=['GET','POST'])
def post_data():
    global counter
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
    return str(counter)


if __name__ == '__main__':
    print('main runned')
    #app.run()
    app.run(debug=True, host='127.0.0.1', port=5701)