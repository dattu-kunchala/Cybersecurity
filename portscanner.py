# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 10:37:55 2021

@author: Dattu
"""

import socket
 
s = socket.socket()
 
result = s.connect_ex((YOUR_URL_HERE, 8090))
 
if(result == 0):
  print('Port is open')
else:
  print('Port is closed')