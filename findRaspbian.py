#-*- coding: utf-8 -*-
import platform
import sys
import os
import time
import thread
import socket
def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip
def find_22(ip):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(5)
    try:
        s.connect((ip,22))
        s.sendall(b'hello\r\n\r\n')
        message = s.recv(100)
        if message:
            print ""
            print "%s" % message.decode("utf-8")
    except Exception as err:
        #print "%s:%s"%(ip,err)
        pass

def find_ip(ip_prefix):
    out=sys.stdout
    for i in range(1,256):
        ip = "%s.%s" % (ip_prefix,i)
        out.write("\rscanning %s" % (ip))
        thread.start_new_thread(find_22, (ip,))
        time.sleep(0.1)
    out.flush()
    print "finish"
if __name__ == "__main__":
  print "start time %s"%time.ctime()
  #commandargs = sys.argv[1:]
  #args = "".join(commandargs)
  ip=get_host_ip()
  ip_prefix = '.'.join(ip.split('.')[:-1])
  find_ip(ip_prefix)
  print "end time %s"%time.ctime()
