def linear_search(list,search_item):
    flag=False
    for element in list:
        if element==search_item:
            flag=True
            break
    if flag:
        return f"{search_item} has been found in {list}"
    else:
        return 
        return f"{search_item} has not been found in {list}"
    

list=[10,15,30,70,80,60,20,90,40]
search_item=20
res=linear_search(list,search_item)
print(res)
