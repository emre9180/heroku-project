import json
import time
from flask import Flask,request, jsonify
from datetime import datetime

app = Flask(__name__)
queue = []

@app.route('/', methods=['GET'])
def index():
  res =  {"sunucuip": "http://192.168.46.179:5000","rtsp": "rtsp://admin:L27C7D5E@192.168.1.104:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif" }
  return jsonify(res)

if __name__ == '__main__':
    app.run()
