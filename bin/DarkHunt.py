import sys
import socket
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.progress import track

def portScanner(ip):
  target = socket.gethostbyname(ip)
  border = Table(title='Scanning Target: %s'%(target))
  view = "Scanning started at:" + str(datetime.now())
  border.add_column(view, style="cyan", no_wrap=False)
  try:
    for port in track(range(1,65535),description='scane port '):
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      socket.setdefaulttimeout(1)
      result = s.connect_ex((target,port))
      if result ==0:
        print("\033[1;32mPort {} is open\033[0m".format(port))
      s.close()
  except KeyboardInterrupt:
    exit('\n\033[1;33mプログラムを終了します !\033[0m')
  except socket.gaierror:
    exit("\n Hostname Could Not Be Resolved !")
  except socket.error:
    exit("\n Server not respoding")