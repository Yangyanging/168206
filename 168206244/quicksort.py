import random
def quicksort(array):
	if len(array)<2:
		return array
	else:
		pivot=array[0]
		a=[i for i in array[1:] if i<=pivot]
		b=[i for i in array[1:] if i>pivot]
		return quicksort(a)+[pivot]+quicksort(b)
arr=random.sample(range(20),10)
print(arr)
print(quicksort(arr))