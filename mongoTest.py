import requests
from flask import jsonify
from flask import Flask
from flask import Response
from flask import request
from urllib import parse
from db import *
import json
import requests
import time
import hashlib
import base64

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

def getBody(filepath):
  # ls = base64.b64encode(binaryAudio) 
  # audio = urllib2.urlencoded(ls)
  binfile = open(filepath, 'rb')
  data = {'audio': base64.b64encode(binfile.read())}
  # print(data)
  # print('data:{}'.format(type(data['audio'])))
  # print("type(data['audio']):{}".format(type(data['audio'])))
  return data

if __name__ == '__main__':
  aue = "raw"
  engineType = "sms16k"
  path='testA.wav'
  r = requests.post(URL, headers=getHeader(aue, engineType), data=getBody(path))
  result = r.content.decode('utf-8')
  print(result)