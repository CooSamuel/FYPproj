from flask import jsonify
from flask import Flask
from flask import Response
from flask import request

app = Flask(__name__)

data = [{
      "name": "王大锤",
      "age": 39,
      "gender": 'F',
      "telephone": 18602987866,
      "complaint": "狄丽丽",
      "ill": "无",
      "diagnosis": "患者2015年10月1日喝酒后上胀痛不适，在无锡市第二人民医院就诊，行CT示：1、肝多发占位，考虑原发性肝癌可能性大；2、肝硬化；3、胆囊小结石；4、双肺纤维灶。查血示：甲胎蛋白：261.31ng/ml、铁蛋白：527.0ng/mL、糖类抗原19-9:61.71U/mL。考虑肝脏多发肿瘤，无手术切除指证，为求进一步治疗，遂至我院就诊，拟“肝恶性肝癌”收住入院。患者病程中无发热，稍感腹胀，无咳嗽咳痰，无胸闷气喘，无恶心呕吐，无腹痛腹泻，无尿急尿频，食纳睡眠可，二便正常，近期体重无明显下降。",
    },
{
      "name": "狗十三",
      "age": 43,
      "gender": "M",
      "telephone": 186089873667,
      "complaint": "哔哩哔哩",
      "ill": "无",
      "diagnosis": "现病史:患者2015年10月1日喝酒后上胀痛不适，在无锡市第二人民医院就诊，行CT示：1、肝多发占位，考虑原发性肝癌可能性大；2、肝硬化；3、胆囊小结石；4、双肺纤维灶。查血示：甲胎蛋白：261.31ng/ml、铁蛋白：527.0ng/mL、糖类抗原19-9:61.71U/mL。考虑肝脏多发肿瘤，无手术切除指证，为求进一步治疗，遂至我院就诊，拟“肝恶性肝癌”收住入院。患者病程中无发热，稍感腹胀，无咳嗽咳痰，无胸闷气喘，无恶心呕吐，无腹痛腹泻，无尿急尿频，食纳睡眠可，二便正常，近期体重无明显下降。",
      },
    {
    "name": "钱安门",
    "age": 78,
    "gender": 'F',
    "telephone": 17863749283,
    "complaint": "阿拉啦啦啦",
    "ill": "有一点，不能说",
    "diagnosis": "现病史:患者2008年10月因右上腹痛就诊当地医院急诊B超示肝占位、腹腔积液，遂诊断为肝肿瘤破裂出血、出血性休克，急诊入我院行介入肝动脉栓塞，术中诊断“肝恶性肿瘤破裂出血，原发性肝癌”，术后恢复可后出院，08-12再次至我院行TACE术一次。2009年1月于上海东方肝胆医院行右肝肿瘤切除及胆囊切除术，术后病理为坏死性肝癌。随访多次复查AFP、影像学检查均未见明显异常变化。2013-09月复查MRI，肝内出现新病灶，分别于09月、11月行TACE两次及肝肿瘤射频消融术两次治疗，2014年2月、5月、10月及20153月于我科复查MRI未见肿瘤复发征象，现患者为行再次复查入我科。近期患者一般情况良好，食纳可，睡眠可，二便正常，无发热咳嗽，无腹痛腹泻，体重无明显变化。"
    },
  {
    "name": "qianmen",
    "age": 78,
    "gender": 'F',
    "telephone": 17863749283 ,
    "complaint": "complaint",
    "ill": "ill",
    "diagnosis": "peiwomenchifanhaohaochiya"
    }
    ]

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

@app.route("/")
def hello():
  resp = Response()
  resp.headers['Access-Control-Allow-Origin'] = '*'
  return resp

if __name__ == '__main__':
  app.run(host="0.0.0.0", port=5000)

#key: 1, name: 'John Brown', age: 32, address: 'New York No. 1 Lake Park', 
# description: 'My name is John Brown, I am 32 years old, living in New York No. 1 Lake Park.',

