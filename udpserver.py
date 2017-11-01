#!/usr/bin/python3
# -*- coding:UTF-8 -*-
from socket import *
from time import ctime
from os import *
HOST = ''
PORT = 8888
BUFSIZ = 128
ADDR = (HOST, PORT)
udpServer = socket(AF_INET, SOCK_DGRAM)
udpServer.bind(ADDR)
while True:
    print 'waiting for message...'
    data, addr = udpServer.recvfrom(BUFSIZ)
    print 'get msg:',data
    power_command=data.split('_')[0]
    pin_number=data.split('_')[1]
    if(power_command=='on'):
      print 'on:',pin_number
      system('sudo ./power.sh %s %s' % (pin_number,1))
    if(power_command=='off'):
      print 'off:',pin_number
      system('sudo ./power.sh %s %s' % (pin_number,0))
    udpServer.sendto('[%s] %s' % (ctime(), data), addr)
    print '...received from and returned to:', addr
udpServer.close()
