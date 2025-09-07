
num = int(input("Enter any three digit number: "))
sum = 0
temp = num
def is_armstrong(num):
    temp=num
    while num>0:
        d=num%10
        sum=sum+d**3
        num=num//10
    if temp==sum:
        return True
    else:
        return False

res=is_armstrong(num)
if res:
    print("Armstrong")
else:
    print("Not Armstrong")

