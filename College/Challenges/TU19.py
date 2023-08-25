#TU19
file = '/Users/ramboozle/Library/Mobile Documents/com~apple~CloudDocs/Coding/School Work/Things used for code/Read, Write & append/counter.txt'

with open(file,"w") as new_file:
    for i in range(11):
        new_file.write(str(10-i)+' ')