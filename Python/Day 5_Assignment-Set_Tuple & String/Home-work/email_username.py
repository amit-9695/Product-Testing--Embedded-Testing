email=input("Enter your Email : ")
at_pos=email.find('@')
print(at_pos)
user_name=email[ :at_pos]
print(f"user name : {user_name}")
dot_find=email.rfind(".")
print(dot_find)
server_name=email[at_pos+1:dot_find]
print(f"server name: {server_name}")
domain_name=email[dot_find+1 :]
print(f"domain name: {domain_name}")