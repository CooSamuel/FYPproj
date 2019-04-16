from flask import jsonify
from flask import Flask
from flask import Response
from flask import request
import json
from db import *

app = Flask(__name__)
dic = {"df": "adf", "ddd":"asd" }
js = jsonify(mm="ddd", mes="hello")
