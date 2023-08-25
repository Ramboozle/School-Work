histograms = [4,2]
counter = 0
temp = ''
for i in range(len(histograms)):
    temp = histograms[counter]
    for x in range(temp):
        print('*',end='')
    print()
    counter=counter+1