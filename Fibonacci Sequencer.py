num = [0,1]
x = int(input("Length of Sequence: "))
for i in range(0, x-2):
    if num == 2:
        num.append(num[0] + num[1])
    else:
        num.append(num[-1] + num[-2])
print(num)


