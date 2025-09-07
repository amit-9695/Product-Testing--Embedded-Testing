# Selection sort takes an unsorted list as a input and output an sorted list
def selection_sort(list):
    for i in range (0,len(list)):
        min=list[i]
        pos=i
        for j in range(i+1,len(list)):
            if list[j]<min:
                pos=j
                min=list[j]
        temp=list[i]
        list[i]=min
        list[pos]=temp
    return list

list=[10,90,60,80,70]
res=selection_sort(list)
print(res)     