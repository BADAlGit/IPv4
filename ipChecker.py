def validIPAddress( IP):

    blocks = IP.split('.')
    if len(blocks) == 4:
        for i in range(len(blocks)):
            if not blocks[i].isdigit() or not 0 <= int(blocks[i]) < 256 or \
               (blocks[i][0] == '0' and len(blocks[i]) > 1):
                return False
        return True
        

storeIp = []

for i in range(10):
    IPv4 = input("Enter IPv4: ")
    if(validIPAddress(IPv4)==True):
        storeIp.append(IPv4)
	print("Valid IPv4 Adress. Enter next{after pressing enter key}."
        continue
    else:
        print("It is not a validIPAddress")
        # break
 
for i in range(len(storeIp)): 
    print(storeIp[i])

# 256.256.256.256 : Not a valid Ipv4 address
# 172.16.254.1 : valid Ipv4 address