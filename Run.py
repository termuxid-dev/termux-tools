#!/usr/bin/python

from os import system as bash
from sys import exit as keluar
from bin import Rio,DarkHunt

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
    print("can't install module")
def pilih():
  pilih_menu = input("enter your choice : ")
  if pilih_menu in ['01','1']:
    IP = input("\nIP TARGET : ")
    PORT = int(input("PORT TARGET: "))
    Rio.AttackIp(IP,PORT)
  elif pilih_menu in ['02','2']:
    URL = input("\nURL TARGET : ")
    AMOUNT = int(input("AMOUNT TARGET: "))
    Rio.AttackUrl(URL,AMOUNT)
  elif pilih_menu in ['03','3']:
    IP = input("\nIP : ")
    DarkHunt.portScanner(IP)
  elif pilih_menu in ['0','00']:
    bash('rm  $HOME/.termux/colors.properties')
    bash('rm  $HOME/.termux/font.ttf')
    bash('termux-reload-settings')
    exit('\nまたね !')
  else:
    print('\033[1;31mpilih yang ada di menu !\033[0m');
def hapus():
  bash('clear')
def main():
  bash('cp colors.properties $HOME/.termux/')
  bash('cp font.ttf $HOME/.termux/')
  bash('termux-reload-settings')
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
  table.add_column(logo, style="cyan", no_wrap=False)
  table.add_row("1. DDOS IP  3. PORT SCANNER")
  table.add_row("2. DDOS URL")
  table.add_row("0. EXIT")
  console = Console()
  hapus()
  console.print(table)
  pilih()
main()