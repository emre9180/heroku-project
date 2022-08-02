import json
import time
from flask import Flask,request, jsonify
from datetime import datetime

app = Flask(__name__)
queue = []

@app.route('/', methods=['GET'])
def index():
  res =  {"sunucuip": "http://192.168.1.52:5000","rtsp": "rtsp://192.168.1.41:554/1/1"

if __name__ == '__main__':
    app.run()
