# temp_read

basic temperature reader/writer using DHT22 Temp/Humidity Sensor and ThingSpeak.

# Python Dependencies

    sudo apt update; sudo apt upgrade
    sudo apt install python-pandas
    sudo pip install adafruit_python_dht
    sudo pip install pyyaml

# Crontab

    */10 * * * * cd ~/brigantine; python record_send.py

## Thingspeak API

Put the thingspeak API in config.yml

    thinkspeak: '{THINGSPEAK_WRITE_API}'

## Pins

The default pins are `4` for the temperature/humidity and `22` for the water sensor.
