import json
import time
from flask import Flask,request, jsonify
from datetime import datetime

app = Flask(__name__)
queue = []

@app.route('/', methods=['GET'])
def index():
  res =  {"sunucuip": "http://192.168.1.52:5000","rtsp": "rtsp://admin:Eyedius2019@192.168.1.99:554/ch01/0,rtsp://admin:Eyedius2021@192.168.1.110:554/cam/realmonitor?channel=1&subtype=1&unicast=true&proto=Onvif,rtsp://192.168.1.29:554/ch01.264?dev=1,rtsp://192.168.1.38:554/ch01.264?dev=1,rtsp://admin:@192.168.1.15:554/live/0/MAIN,rtsp://admin:L27C7D5E@192.168.1.104:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif,rtsp://admin:123456@192.168.1.13:554/stream1,rtsp://admin:123456@192.168.1.153:554/stream1"}

if __name__ == '__main__':
    app.run()
