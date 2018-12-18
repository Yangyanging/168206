
def guibing(lis1,lis2):
    lis3=[]
    i=j=0
    while i<len(lis1) and j<len(lis2):
        if lis1[i]<lis2[j]:
            lis3.append(lis1[i])
            i+=1
        else:
            lis3.append(lis2[j])
            j+=1
    if i==len(lis1):
        for a in lis2[j:]:
            lis3.append(a)
    else:
        for a in lis1[i:]:
            lis3.append(a)
    return lis3        
def merge_sort(lists):
    if len(lists)<=1:
        return lists
    mid=len(lists)//2
    left=merge_sort(lists[:mid])
    right=merge_sort(lists[mid:])
    return guibing(left, right)


if __name__=="__main__":
    alist=[5,7,3,0,2,4,90,8,80,999,9]
    print(merge_sort(alist))