arrays = []
temp = []
count = 1
pascal = int(input("Height of Pascal Triangle: "))

while count < pascal+1:
    temp = []
    for i in range (count):
        if i == 0:
            temp.append(1)
        elif i == count - 1:
            temp.append(1)
        else:
            temp.append(arrays[i] + arrays[i - 1])
    arrays = temp[:]
    print(temp)
    count += 1


