#!/usr/bin/python2
import os
import yaml
import sys
import Adafruit_DHT
import requests
from datetime import datetime,timedelta


def measure_the_data():
    sensor = Adafruit_DHT.AM2302
    pin = 4
    humidity, temp_c = Adafruit_DHT.read_retry(sensor, pin)
    print(temp_c,humidity)
    if temp_c!=None:
        temp_f = 9.0/5.0 * temp_c + 32
        return temp_f,humidity
    else:
        return temp_c, humidity

def send_the_data(temp,hum,api_key):
    requests.post('https://api.thingspeak.com/update'+
            '?api_key={}&field1={}&field2={}'.
            format(api_key,round(temp,1),round(hum,1)))

if __name__=='__main__':
    with open('config.yaml','r') as f:
        config = yaml.safe_load(f)
    api_key = config['thinkspeak']
    temp,hum = measure_the_data()
    send_the_data(temp,hum,api_key)
