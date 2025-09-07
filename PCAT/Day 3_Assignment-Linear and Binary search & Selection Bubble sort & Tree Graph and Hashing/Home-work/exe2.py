def linear_search(list,target):
    flag=False
    index=-1
    for i in range(0,len(list)):
        if list[i]==target:
            flag=True
            index=i
            break
    if flag==True:
        print(target," is found at ",index, " positin in the list")
    else:
        print(target," is not found in the list ")
        

#calling
linear_search([10,20,30,40,50],20)
