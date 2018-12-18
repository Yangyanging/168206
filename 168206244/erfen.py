def binary_serach(list, item):
	low=0
	high=len(list)-1
	while low<=high:
		mid=int((low+high)/2)
		guess=list[mid]
		if guess==item:
			return mid
		if guess>item:
			print(guess,"大了")
			high=mid-1
		else:
			print(guess,"小了")
			low=mid+1
	return None
#my_list=[1,3,5,7,9,11,13,15]

def diguierfen(list,item):
	mid=len(list)//2
	if list[mid]==item:
		return list[mid]
	if mid==0:
		return 0
	else:
		if item>list[mid]:
			return diguierfen(list[mid:],item)
		else:
			return diguierfen(list[:mid],item)
        
lis=[1,3,5,7,9,11,13,15]
print(lis)
x=int(input("请输入要找的数字:"))
print(diguierfen(lis,x)) 