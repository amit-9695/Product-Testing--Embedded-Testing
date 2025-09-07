""" 
Given a list of numbers, write a python function to exchange the first n/2 elements of a list with the last n/2 elements. The function should return the new list.
n represents the number of elements in the list. Assume that it will always be even.
Sample Input
Expected Output
[1,2,3,4,5,6,7,8,9,10]
[10,9,8,7,6,1,2,3,4,5]
"""

def exchange_elements(lst):
    n = len(lst)
    mid = n // 2
    print("for lst[mid:]: ", lst[mid:])
    print("for lst[:mid]: ", lst[:mid])
    
    mid1 = lst[:mid]
    temp = lst[mid:]
    mid2 = []
   # append all element of temp in mid 2 in desending order
    for i in range(len(temp)-1, -1, -1):
        mid2.append(temp[i])    
        
    
    return mid2 + mid1

# Example usage
if __name__ == "__main__":
    sample_input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = exchange_elements(sample_input)
    print(result)
    