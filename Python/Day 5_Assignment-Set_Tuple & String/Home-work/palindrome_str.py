str=input("Enter any word :")
def palindrom(str):
    if str[ : : -1]==str[ : ]:
        return True
    return False

res=palindrom(str)
if res:
    print(f"The given string - {str} is palindrome")
else:
    print(f"The given string - {str} is not palindrome")