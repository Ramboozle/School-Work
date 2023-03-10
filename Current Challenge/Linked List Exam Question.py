startpointer = 0
emptylist = 5

class node():
    def __init__(self,data,nextnode):
        self.data = data
        self.nextnode = nextnode

    def __repr__(self):
        return str(self.data)

def outputNodes(startpointer,linkedList):
    data = []
    next = []
    data.append(linkedList[startpointer])
    startpointer = linkedList[startpointer].nextnode
    for i in range(len(linkedList)):
        data.append(linkedList[startpointer])
        startpointer = linkedList[startpointer].nextnode
    data.append(linkedList[startpointer])

    startpointer = 0
    next.append(linkedList[startpointer].nextnode)
    startpointer = linkedList[startpointer].nextnode
    for i in range(len(linkedList)):
        next.append(linkedList[startpointer].nextnode)
        startpointer = linkedList[startpointer].nextnode
    next.append(linkedList[startpointer].nextnode)

    print('data values',data)
    print('next values',next)

def addNode(linkedList,emptylist):
    data = input('What data do you want to add?')
    linkedList[emptylist].data = data
    next = emptylist
    linkedList.append(node(data,next))


linkedList = [node(1,1), node(5,4), node(6,7), node(7,-1),
              node(2,2), node(0,6), node(0,8), node(56,3),
              node(0,9), node(0,-1)]

outputNodes(startpointer,linkedList)
addNode(linkedList,emptylist)
outputNodes(startpointer,linkedList)