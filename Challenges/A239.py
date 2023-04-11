queue = [1,2,4,5,6,6,6,9]

def EnQueue(input):
    queue.append(input)
    print('Added',input,'to the queue')

def DeQueue():
    if len(queue) == 0:
        print('Queue is empty')
    else:
        print('Removed',queue[0],'from the queue')
        queue.remove(queue[0])

print(queue)
DeQueue()
print(queue)
EnQueue(10)
print(queue)