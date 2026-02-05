# file = open("order.txt","w")
# try:
#     file.write("hello This is your weapon arsenal") 
# finally:
#     file.close()


with open("order.txt",'w') as file:
    file.write("AK will be ordered for you.")