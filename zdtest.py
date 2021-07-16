# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 12:56:03 2021

@author: Dattu
"""

import zdm
import random
import time

def pub_temp_hum():
    # this function publish into the tag weather two random values: the temperature and the humidity
    tag = 'weather'
    temp = random.randint(19, 38)
    hum = random.randint(50, 70)
    payload = {'temp': temp, 'hum': hum}
    device.publish(payload, tag)
    print('Published: ', payload)


# connect to the ZDM using credentials in zdevice.json file
device = zdm.ZDMClient()
device.connect()

# infinite loop
while True:
    pub_temp_hum()
    time.sleep(5)