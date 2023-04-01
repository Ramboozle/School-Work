#TU18
import time

file = '/Users/ramboozle/Library/Mobile Documents/com~apple~CloudDocs/Coding/School Work/Things used for code/Read, Write & append/rudyard.txt'

with open(file,"r") as whole_file:
   for line in whole_file:
        print(line,end="")
        time.sleep(3)