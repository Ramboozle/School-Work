class Test:

    def __init__(self,name):
        self.name = name
        print(self.name)

    def __repr__(self):
        return str(self.name)
numbers = [1,2,3,4,5,6,7,8,9,10]
list = []
for i in range(10):
    list.append(Test(numbers[i]))
print(list)