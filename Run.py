#!/usr/bin/python

from os import system as bash
from sys import exit as keluar
try :
  from requests import get as deteksiIp
  from rich.console import Console
  from rich.table import Table
except ImportError:
  bash('pip install requests')
  bash('pip install rich')
  try:
    from requests import get as deteksiIp
    from rich.console import Console
    from rich.table import Table
  except ImportError:
    print('tidak dapat menginstal module')
def pilih():
  pilih_menu = input("pilih : ")
  if pilih_menu in ['01','1']:
    IP = input("\nIP TARGET : ")
    PORT = input("PORT TARGET: ")
    bash("python ./DdoS/IP.py %s %s"%(IP,PORT))
  elif pilih_menu in ['02','2']:
    URL = input("\nURL TARGET : ")
    AMOUNT = input("AMOUNT TARGET: ")
    bash("python ./DdoS/Url.py %s %s"%(URL,AMOUNT))
  elif pilih_menu in ['0','00']:
    exit('\nまたね !')
  else:
    print('\033[1;31mpilih yang ada di menu !\033[0m');

def hapus():
  bash('clear')

def main():
  re = deteksiIp('https://api.myip.com').json()
  ip = re['ip']
  table = Table(title="my ip: %s"%(ip))
  logo = """
▀▀█▀▀ █▀▀█ █▀▀█ █── █▀▀ 
─░█── █──█ █──█ █── ▀▀█ 
─░█── ▀▀▀▀ ▀▀▀▀ ▀▀▀ ▀▀▀
  Termux-Tools || Termux Indonesia
  _______________________________
  """
  # ada jepang 🤭🤣
  table.add_column(logo, style="cyan", no_wrap=True)
  table.add_row("1. DDOS IP")
  table.add_row("2. DDOS URL")
  table.add_row("0. EXIT")
  console = Console()
  hapus()
  console.print(table)
  pilih()
main()