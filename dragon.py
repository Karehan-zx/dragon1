import string
import os
import time
os.system("clear")
print("      [+] Starting ....")
time.sleep(1)
os.system("clear")
os.system("cd /data/data/com.termux/files/usr/bin && ls")
c = str(input("/*_*/~@dragon/~》》"))
if c == "" :
    os.system("clear")
    print("\n         [+] exiting ......")
    time.sleep(1)
    print("\n         [+] 😉 goog bye .....")
    exit()
else :
    get = False
try :
    opt = str("/data/data/com.termux/files/usr/bin"+"/"+c) 
    file = open(opt)
    get = True 
except :
          FileNotFoundError
if get == True :
    i = 0
    os.system("clear")
    print("\n         [+] loading ......")
    time.sleep(1)
    os.system(c+" --help")
else :
    i = 1
while i == 0 :
    c2 = str(input("/*_*/~@dragon/~"+"@"+c+"~》》"))
    if   c2 == "exit" :
      os.system("clear")
      break
    else :
      os.system(c + " " + c2)  
if get == False :
  print("error")
  print("\n                   [+] loading .....")
  time.sleep(1)
else :
  print("\n                   [+] loading ......")
  time.sleep(1)
os.system("dragon")
 
 
