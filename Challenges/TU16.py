Ringgit=float(129)
print(f'RM{Ringgit}')

numbers1 = [1,2,3]
numbers2 = [4,5,6]
numbers3 = [7,8,9]
numbers4= [10,11,12]
print("A table with numbers in")
for i in range(3):
    print(f"{numbers1[i]:^20} {numbers2[i]:^20} {numbers3[i]:^20} {numbers4[i]:^20}")

num=int(input('input your number to be converted'))
print(f"Binary: {num:b}\nHexadecimal: {num:x}\nDecimal: {num:d}")