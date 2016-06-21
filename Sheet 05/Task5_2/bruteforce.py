import hashlib
import binascii

path = 'rfc7511.txt'

messageauthenticator = '45b6c0810adffb1df0af6a0e41533c4c'

userpasswordattribute = 'b89aac246a9694c177081c099dfc1f0e'

nonce = 'c05e767c28001ef3800526a8306a55445262e4b6f45df41b18061cbe'

pw = ''


noncetogo = binascii.unhexlify(nonce)

print nonce.decode("hex")



check = False
file = open(path, 'r')
for line in file:
    for word in line.split():
        conc = word + nonce
        m = hashlib.md5()
        m.update(conc)

        c = m.hexdigest() ^ binascii.hexlify(pw)

        if(userpasswordattribute == c):
            check = True
print check