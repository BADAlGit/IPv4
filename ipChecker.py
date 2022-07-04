def validIPAddress( IP):

    blocks = IP.split('.')
    if len(blocks) == 4:
        for i in range(len(blocks)):
            if not blocks[i].isdigit() or not 0 <= int(blocks[i]) < 256 or \
               (blocks[i][0] == '0' and len(blocks[i]) > 1):
                return False
        return True
        

storeIp = []

for i in range(2):
    IPv4 = input("Enter IPv4: ")
    if(validIPAddress(IPv4)==True):
        binaryValue = '.'.join([bin(int(x)+256)[3:] for x in IPv4.split('.')]) 
        octalValue ='.'.join(["%04o" % int(x) for x in IPv4.split('.')])
        hexaValue = '.'.join([hex(int(i))[2:] for i in IPv4.split('.')])
        storeIp.append(IPv4, binaryValue, octalValue, hexaValue))
        continue
    else:
        print("It is not a validIPAddress")
        # break
 
for i in range(len(storeIp)): 
    print(storeIp[i])

# 256.256.256.256 : Not a valid Ipv4 address
# 172.16.254.1 : valid Ipv4 address