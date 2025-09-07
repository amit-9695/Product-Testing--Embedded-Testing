def merge_sort(num_list):
    # Remove pass and write the logic here to return the sorted list




    pass


def merge(left_list,right_list):
    # Remove pass and write the logic to merge the elements in the left_list and right_list and return the sorted list
    pass


num_list=[34, 67, 8, 19, 2, 23, 1, 91]
print("Before sorting:",num_list)
sorted_list = merge_sort(num_list)
print("After sorting:",sorted_list)

# Divide the Array. the array is divided into two halves
# Divide Each half. Continue dividing each half into smaller subarray until each subarray has only one element.
# Merge Each pair of subarrays
# Merge the sorted subarrays
# Merge the final two halves
#final sorted


# take two sorted list as input & return as sorted list as an output
def merge_arrays(arr1,arr2):
    i=0
    j=0
    k=0
    l1=len(arr1)
    l2=len(arr2)
    arr3=[]
    while i<l1 and j<l2:
        #pick smaller of the two current elements and move ahead in the array of the picked element
        if(arr1[i]<arr2[j]):
            arr3.append(arr1[i])
            i=i+1
        else:
            arr3.append(arr2[j])
            j=j+1
    # if there are remaining elements of the first array, move them
    while i<l1:
        arr3.append(arr1[i])
        i=i+1
    
    #Else if there are remaining elements of the second array move them
    while j<l2:
        arr3.append(arr2[j])
        j=j+1
    return arr3


def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left_arr=arr[:mid]
    right_arr=arr[mid:]
    left_arr= merge_sort(left_arr)
    right_arr=merge_sort(right_arr)
    return merge_arrays(left_arr,right_arr)


sorted_list=merge_sort([2,7,1,8,6])
print(sorted_list)