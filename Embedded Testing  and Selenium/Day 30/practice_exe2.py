""" 
Write a python function which accepts a list of strings containing details of deposits and withdrawals made in a bank account and returns the net amount in the account.
Suppose the following input is supplied to the function 
["D:300","D:300","W:200","D:100"] where D means deposit and W means withdrawal,
then the net amount in the account is 500.
 
Sample Input
["D:300","D:200","W:200","D:100"]
["D:350","W:100","W:500","D:1000"]
	
Expected Output
400
750
"""
def calculate_net_amount(transactions):
    net_amount = 0
    for transaction in transactions:
        type_, amount = transaction.split(":")
        amount = int(amount)
        if type_ == "D":
            net_amount += amount
        elif type_ == "W":
            net_amount -= amount
    return net_amount

# Sample usage
print(calculate_net_amount(["D:300", "D:200", "W:200", "D:100"]))   
print(calculate_net_amount(["D:350", "W:100", "W:500", "D:1000"])) 