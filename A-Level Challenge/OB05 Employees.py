dir = '/Users/ramboozle/Library/Mobile Documents/com~apple~CloudDocs/Coding/School Work/Things used for code/emailList.txt'
class Employees:
    def __init__(self,firstname,lastname,fullname,email,employeeid):
        self.__FirstName = firstname
        self.__LastName = lastname
        self.__FullName = fullname
        self.__Email = email
        self.__EmployeeID = employeeid

    def __repr__(self):
        return self.__FirstName,self.__LastName,self.__FullName,self.__Email,self.__EmployeeID

    def GetEmployeeEmail(self):
        return self.__EmployeeID,self.__Email

    def PrintDetails(self):
        print(self.__FirstName,self.__LastName,self.__FullName,self.__Email,self.__EmployeeID)

EmployeeArray = []

with open(dir,'r') as f:
    LineCount = len(f.readlines())
    f.seek(0)
    for i in range(int(LineCount/2)):
        first = f.readline().strip()
        last = f.readline().strip()
        fullname = first+' '+last
        email = first+last+'@company.com'
        empid = i+1
        EmployeeArray.append(Employees(first,last,first+last,email.lower(),empid))

for i in range(len(EmployeeArray)):
    print(EmployeeArray[i].PrintDetails())