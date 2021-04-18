#!/usr/bin/python
import yaml
import sys
import Adafruit_DHT
import requests
sensor = Adafruit_DHT.DHT22
pin = 4
print(Adafruit_DHT.read_retry(sensor, pin))
