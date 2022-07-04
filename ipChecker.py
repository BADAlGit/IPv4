import pickle


def validIPAddress(IP):

    blocks = IP.split('.')
    if len(blocks) == 4:
        for i in range(len(blocks)):
            if not blocks[i].isdigit() or not 0 <= int(blocks[i]) < 256 or \
               (blocks[i][0] == '0' and len(blocks[i]) > 1):
                return False
        return True


storeIp = []
n = int(input("Enter total number of IPv4 adresses: "))
for i in range(n):
    IPv4 = input("Enter IPv4: ")
    if(validIPAddress(IPv4) == True):
        binaryValue = '.'.join([bin(int(x)+256)[3:] for x in IPv4.split('.')])
        octalValue = '.'.join(["%04o" % int(x) for x in IPv4.split('.')])
        hexaValue = '.'.join([hex(int(i))[2:] for i in IPv4.split('.')])
        storeIp.append((IPv4, binaryValue, octalValue, hexaValue))
        continue
    else:
        print("It is not a validIPAddress")
        # break
# for i in storeIp:
#     print(i)

f = open('conversion.txt', 'w')
for t in storeIp:
    line = ', '.join(str(x) for x in t)
    f.write(line + '\n')
f.close()

IPFile = open('conversion.txt', 'r')
# Lines = file1.readlines()
count = 0
for line in IPFile:
    count += 1
    print("The {} adreess om Decimal, Binary, Octal and Hexadecimal format is : {}".format(
        count, line.strip()))

# Closing files
IPFile.close()
