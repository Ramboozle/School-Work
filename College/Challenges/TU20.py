#TU20
file = '/Users/ramboozle/Library/Mobile Documents/com~apple~CloudDocs/Coding/School Work/Things used for code/Read, Write & append/counter.txt'

with open(file, "r") as existing_file:
    for line in existing_file:
        for word in line.split():
            lastnum = int(word)

with open(file,"a") as existing_file:
    lastnum = int(lastnum) + 1
    for i in range(9):
        lastnum = lastnum + 1
        existing_file.write(str(lastnum)+"\n")