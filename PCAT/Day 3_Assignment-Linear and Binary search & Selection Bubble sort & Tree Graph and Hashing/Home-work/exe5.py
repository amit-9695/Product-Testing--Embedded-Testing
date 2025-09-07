def bubbleSort(arr):
    for i in range(0,len(arr)):
        for j in range(0,len(arr)-i-1):
            if (arr[j]>arr[j+1]):
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
    return arr

#calling
sorted_arr=bubbleSort([4,7,8,1,2,111])
print(sorted_arr)
