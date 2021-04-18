#!/usr/bin/python2
import time
import os
import yaml
import sys
import RPi.GPIO as GPIO
import requests
from datetime import datetime,timedelta


def measure_the_data(channel):
    return GPIO.input(channel)

def send_the_data(is_dry,api_key):
    requests.post('https://api.thingspeak.com/update'+
            '?api_key={}&field3={}'.
            format(api_key,round(is_dry)))

if __name__=='__main__':
    channel=22
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(channel, GPIO.IN)
    GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
    with open('config.yaml','r') as f:
        config = yaml.safe_load(f)
    api_key = config['thinkspeak']
    is_dry = measure_the_data(channel)
    send_the_data(is_dry,api_key)
    print is_dry

