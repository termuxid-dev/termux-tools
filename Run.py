import requests
import os
import sys

def checkip():
 print('[!] GET IP..')
 re = requests.get('https://api.myip.com').json()
 ip = re['ip']
 print('[!] IP you : {ip}')
 
def ddos():
 print('''
     [Menu DDOS Attack]
[1] DDOS IP
[2] DDOS URL
[3] Return
''')
menu_ddos = input('[?] Please select the menu : ')

def ddos_url():
    input_url = raw_input('[DDOS IP] Enter Target URL :')
    input_amount = input('[DDOS IP] Enter Amount :')

    if input_url == True:
 os.system('cd DdoS')
 os.system('python2 URL.py {input_url} {input_amount}')
 else:
 print('[!] Target URL failed not entered')
 sys.exit()

def ddos_ip():
    input_ip = raw_input('[DDOS IP] Enter Target IP :')
    input_port = input('[DDOS IP] Enter Port :')

    if input_ip == True:
 os.system('cd DdoS')
 os.system('python2 IP.py {input_ip} {input_port}')
 else:
 print('[!] Target IP failed not entered')
 sys.exit()
 
 os.system("clear")
os.system("figlet Termuxid Tools")
print
print "Author   : Termuxid"
print "TEAM     : Termux Indonesia"
print "Thanks   : All Member Termux Indonesia"
print "Tingkat  : Programmer & Developer"
print "https://termuxid.dev"
print

print('''
     [Menu]
[1] Check IP
[2] DDOS Attack
[3] Logout
''')
menu = input('[?] Please select the menu : ')

if menu == '1':
 checkip()
elif menu == '2':
 ddos()
elif menu == '3':
 print('[?] Logot..')
 sys.exit()
else:
 print('[?] Unknown command..')
 sys.exit()

if menu_ddos == '1':
 ddos_ip()
elif menu_ddos == '2':
 ddos_url()
elif menu_ddos == '3':
  os.system('python2 run.py')
else:
 print('[?] Unknown command..')
 sys.exit()