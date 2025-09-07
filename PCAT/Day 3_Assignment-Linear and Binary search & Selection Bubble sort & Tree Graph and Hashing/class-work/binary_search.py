def binary_search(list,searching_element):
    # Initilly we assuming that searching_elemnt is not present in list
    flag = False
    start=0
    end=len(list)-1
    while (start<=end):
        mid=(start+end)//2
        if searching_element>list[mid]:
            start=mid+1
        elif searching_element<list[mid]:
            end=mid-1
        else:
            flag=True
            break
    return flag

list=[10,20,30,40,50]
searching_element=40
res=binary_search(list,searching_element)
if res:
    print("We find Searching Element")
else:
    print("We can't find searching element")
