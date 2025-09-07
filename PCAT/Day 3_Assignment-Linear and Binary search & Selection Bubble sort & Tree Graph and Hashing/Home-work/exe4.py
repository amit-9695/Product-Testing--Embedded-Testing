def selection_sort(arr):
     for i in range(0,len(arr)):
         # Assume the current position holds
         #the minimum element
         min=arr[i]
         pos=i
         for j in range(i+1,len(arr)):
             if arr[j]<min:
                 min=arr[j]
                 pos=j
         temp=arr[i]
         arr[i]=min
         arr[pos]=temp
     return arr
 
 #calling
sorted_arr=selection_sort([2,6,7,9,1])
print(sorted_arr)

sorted_arr=selection_sort([10,31,45,67,80])         
print(sorted_arr)
