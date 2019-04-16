from flask import jsonify
from flask import Flask
from flask import Response
from flask import request
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


app = Flask(__name__)

data = [{
      "userinfo" :{
        "name": "王大锤",
        "age": 39,
        "gender": 'F',
        "telephone": 18602987866,
      },
      "complaint": "狄丽丽",
      "ill": "无",
      "diagnosis": "患者2015年10月1日喝酒后上胀痛不适，在无锡市第二人民医院就诊，行CT示：1、肝多发占位，考虑原发性肝癌可能性大；2、肝硬化；3、胆囊小结石；4、双肺纤维灶。查血示：甲胎蛋白：261.31ng/ml、铁蛋白：527.0ng/mL、糖类抗原19-9:61.71U/mL。考虑肝脏多发肿瘤，无手术切除指证，为求进一步治疗，遂至我院就诊，拟“肝恶性肝癌”收住入院。患者病程中无发热，稍感腹胀，无咳嗽咳痰，无胸闷气喘，无恶心呕吐，无腹痛腹泻，无尿急尿频，食纳睡眠可，二便正常，近期体重无明显下降。",
    },
    {
      "userinfo" :{
        "name": "狗十三",
        "age": 43,
        "gender": "M",
        "telephone": 186089873667,
      },
      "complaint": "哔哩哔哩",
      "ill": "无",
      "diagnosis": "现病史:患者2015年10月1日喝酒后上胀痛不适，在无锡市第二人民医院就诊，行CT示：1、肝多发占位，考虑原发性肝癌可能性大；2、肝硬化；3、胆囊小结石；4、双肺纤维灶。查血示：甲胎蛋白：261.31ng/ml、铁蛋白：527.0ng/mL、糖类抗原19-9:61.71U/mL。考虑肝脏多发肿瘤，无手术切除指证，为求进一步治疗，遂至我院就诊，拟“肝恶性肝癌”收住入院。患者病程中无发热，稍感腹胀，无咳嗽咳痰，无胸闷气喘，无恶心呕吐，无腹痛腹泻，无尿急尿频，食纳睡眠可，二便正常，近期体重无明显下降。",
      },
    {
      "userinfo" :{
        "name": "钱安门",
        "age": 78,
        "gender": 'F',
        "telephone": 17863749283,
      },
    "complaint": "阿拉啦啦啦",
    "ill": "有一点，不能说",
    "diagnosis": "现病史:患者2008年10月因右上腹痛就诊当地医院急诊B超示肝占位、腹腔积液，遂诊断为肝肿瘤破裂出血、出血性休克，急诊入我院行介入肝动脉栓塞，术中诊断“肝恶性肿瘤破裂出血，原发性肝癌”，术后恢复可后出院，08-12再次至我院行TACE术一次。2009年1月于上海东方肝胆医院行右肝肿瘤切除及胆囊切除术，术后病理为坏死性肝癌。随访多次复查AFP、影像学检查均未见明显异常变化。2013-09月复查MRI，肝内出现新病灶，分别于09月、11月行TACE两次及肝肿瘤射频消融术两次治疗，2014年2月、5月、10月及20153月于我科复查MRI未见肿瘤复发征象，现患者为行再次复查入我科。近期患者一般情况良好，食纳可，睡眠可，二便正常，无发热咳嗽，无腹痛腹泻，体重无明显变化。"
    },
    {
    "userinfo" :{
      "name": "qianmen",
      "age": 78,
      "gender": 'F',
      "telephone": 17863749283 ,
    },
    "complaint": "complaint",
    "ill": "ill",
    "diagnosis": "peiwomenchifanhaohaochiya"
    }
    ]
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

@app.route("/testAPI")
def testAPI():
  return jsonify(data)

# Users info 
@app.route("/userinfo", methods=['GET'])
def getUserInfo():
  ls = dm.getAll()
  return jsonify(ls)

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

@app.route("/userinfo/<id>", methods=['PUT','DELETE'])
def updateAPI(id):
  if request.method == 'PUT':
    data = request.json
    print(data)
    dm.updateItem(id, data)
    return jsonify(isError=False, message="PUT"), 200
  if request.method == 'DELETE':
    dm.deleteItem(id)
    return jsonify(deleted=id)

@app.route('/dictate', methods=['POST'])
def translateAPI():
  aue = "raw"
  engineType = "sms16k"
  data = request.data.decode('utf-8')
  audio = json.loads(data)
  print(type(audio))
  # print(audio)
  r = requests.post(URL, headers=getHeader(aue, engineType), data=audio)
  result = r.content.decode('utf-8')
  print(result)
  return result

if __name__ == '__main__':
  app.run(host="0.0.0.0", port=5000,debug=True)

#key: 1, name: 'John Brown', age: 32, address: 'New York No. 1 Lake Park', 
# description: 'My name is John Brown, I am 32 years old, living in New York No. 1 Lake Park.',
