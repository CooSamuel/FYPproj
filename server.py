from flask import jsonify
from flask import Flask
from flask import Response
from flask import request
from urllib import parse
from db import *
import json
import cgi
import requests
import time
import hashlib
import base64
import librosa    
import wave
import SingleWave

URL = "http://api.xfyun.cn/v1/service/v1/iat"
APPID = "5caf0bd5"
API_KEY = "dfca8545e3e33f3d86d1b74c63228aa8"


def getHeader(aue, engineType):
    curTime = str(int(time.time()))
    # curTime = '1526542623'
    param = "{\"aue\":\"" + aue + "\"" + ",\"engine_type\":\"" + engineType + "\"}"
    print("param:{}".format(param))
    paramBase64 = str(base64.b64encode(param.encode('utf-8')), 'utf-8')
    print("x_param:{}".format(paramBase64))

    m2 = hashlib.md5()
    m2.update((API_KEY + curTime + paramBase64).encode('utf-8'))
    checkSum = m2.hexdigest()
    print('checkSum:{}'.format(checkSum))
    header = {
        'X-CurTime': curTime,
        'X-Param': paramBase64,
        'X-Appid': APPID,
        'X-CheckSum': checkSum,
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
    }
    print(header)
    return header

def writeBinary(binaryAudio):
  f = open("myVoiceTest.wav", 'wb')
  print(binaryAudio)
  f.write(binaryAudio)
  f.close()

# def getBody(binaryAudio):
#   # ls = base64.b64encode(binaryAudio) 
#   # audio = urllib2.urlencoded(ls)
#   # binfile = open(filepath, 'rb')
#   # data = {'audio': base64.b64encode(binaryAudio)}
#   data = parse.urlencode({'audio': base64.b64encode(binaryAudio)})
#   # data = {'audio': base64.b64encode(binaryAudio)}
#   print("{} \ndata".format(data))
    
#   # print('data:{}'.format(type(data['audio'])))
#   # print("type(data['audio']):{}".format(type(data['audio'])))
#   return data


def getBody(filepath):
    binfile = open(filepath, 'rb')
    data = {'audio': base64.b64encode(binfile.read())}
    # print(data)
    print('data:{}'.format(type(data['audio'])))
    # print("type(data['audio']):{}".format(type(data['audio'])))
    return data

app = Flask(__name__)

dm = DatabaseManager()

@app.after_request
def add_cors_headers(response):
  response.headers.add('Access-Control-Allow-Origin', "*")
  response.headers.add('Access-Control-Allow-Credentials', 'true')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
  response.headers.add('Access-Control-Allow-Headers', 'Cache-Control')
  response.headers.add('Access-Control-Allow-Headers', 'X-Requested-With')
  response.headers.add('Access-Control-Allow-Headers', 'Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, DELETE')
  return response

# Users info 
@app.route("/userinfo", methods=['GET'])
def getUserInfo():
  ls = dm.getAll()
  return jsonify(ls)

# POST to /adduser
@app.route("/adduser", methods=["POST"])
def addUser():
  data = request.json
  name=data["userInfo"]["name"]
  gender=data["userInfo"]["gender"]
  age=data["userInfo"]["age"]
  telephone=data["userInfo"]["telephone"]
  complaint=data["complaint"]
  ill=data["ill"]
  diagnosis=data["diagnosis"]
  result_raw = dm.createItem(name=name, age=age, gender=gender,telephpne=telephone,zhusu=complaint,ill=ill,chubuzhenduan=diagnosis)
  data['_id'] = str(result_raw)
  return jsonify(data)

# update the userinfo of id
# delete the userinfo of id
@app.route("/userinfo/<id>", methods=['PUT','DELETE'])
def updateAPI(id):
  if request.method == 'PUT':
    data = request.json
    # print(data)
    dm.updateItem(id, data)
    return jsonify(isError=False, message="PUT"), 200
  if request.method == 'DELETE':
    dm.deleteItem(id)
    return jsonify(deleted=id)

# POST dictate
@app.route('/dictate', methods=['POST'])
def translateAPI():
  aue = "raw"
  engineType = "sms8k"

  data = request.files['audio']
  blob = data.read()
  writeBinary(blob)
  # print(blob)
  # data = request.form.get('audio')
  # print(data)
  # audio = json.loads(data)['audio']
  # print(type(audio.encode()))
  # print(audio)
  path='myVoiceTest.wav'
  pathOut='newMyVoiceTest.wav'
  SingleWave(path,pathOut)
  # wf1 = wave.open('newmyVoiceTest.wav', 'r')
  # wf = wave.open(path)
  # sw1 = wf1.getsampwidth()
  # sw = wf.getsampwidth()
  # print(sw1)
  # print(sw)
  # y, s = librosa.load('myVoiceTest.wav', sr=16000)
  r = requests.post(URL, headers=getHeader(aue, engineType), data=getBody(pathOut))
  result = r.content.decode('utf-8')
  print(result)
  return result

if __name__ == '__main__':
  app.run(host="0.0.0.0", port=5000,debug=True)

#key: 1, name: 'John Brown', age: 32, address: 'New York No. 1 Lake Park', 
# description: 'My name is John Brown, I am 32 years old, living in New York No. 1 Lake Park.',
