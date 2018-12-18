import random
def findSmall(a1):
    small=a1[0]
    smallindex=0
    for i in range(1,len(a1)):
        if a1[i] < small:
            small = a1[i]
            smallindex=i
    return smallindex

def select(a1):
    newa1=[]
    for i in range(len(a1)):
        small=findSmall(a1)
        newa1.append(a1.pop(small))
    return newa1

a11=random.sample(range(20),10)
print(a11)
print(select(a11))
print('\n')


def selection(list1):
    length=len(list1)
    for x in range(0,length-1):
        smallest=x
        for y in range(x+1,length):
            if list1[y]<list1[smallest]:
                temp=list1[y]
                list1[y]=list1[smallest]
                list1[smallest]=temp
    
    return list1    
mylist=random.sample(range(20),10)
print(mylist)
print(selection(mylist))    