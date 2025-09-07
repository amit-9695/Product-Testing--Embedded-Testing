def binary_search(list,target):
    start=0
    end=len(list)-1
    flag=False
    
    while start<=end:
        mid=(start+end)//2
        if(target>list[mid]):
            start=mid+1
        elif target<list[mid]:
            end=mid-1
        else:
            flag=True
            break
    if flag==True:
        print(target," is found")
    else:
        print(target," is not found")

binary_search([10,20,30,40,50],30)
