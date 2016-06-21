import hashlib
import binascii

path = 'rfc7511.txt'
authenticator = '45b6c0810adffb1df0af6a0e41533c4c'
string2 = 'd4f042b15aadb9d229c2251d14d32365'
nonce = 'c05e767c28001ef3800526a8306a55445262e4b6f45df41b18061cbe'
key = ''


noncetogo = binascii.unhexlify(nonce)

#bla = binascii.unhexlify(string) + binascii.unhexlify(nonce)
#test = hashlib.md5()
#test.update(bla)



check = False
file = open(path, 'r')
for line in file:
    for word in line.split():

        conc = noncetogo + word
        m = hashlib.md5()
        m.update(conc)

        c = m.hexdigest ^ pw

        print c

        if(string2 == m.hexdigest):
            check = True
print check