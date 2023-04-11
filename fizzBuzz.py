for curNum in range(99):
    if curNum % 3 == 0 and curNum % 5 == 0:
        print("FizzBuzz")
    elif curNum % 3 == 0:
        print("Fizz")
    elif curNum % 5 == 0:
        print("Buzz")
    else:
        print(curNum)