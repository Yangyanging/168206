def sumcount(list):
    if list == []:
        return 0
    return list[0] + sumcount(list[1:])

list=[45,15,24,48,15,66]
print(sumcount(list))