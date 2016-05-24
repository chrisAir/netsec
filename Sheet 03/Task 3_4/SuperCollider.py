import os
import hashlib
import prefComparator
import matplotlib.pyplot

loopFlag = True
loopCount = 1

while loopFlag:
    # generate two random byte sequences
    rndSequence1 = bytearray(os.urandom(64))
    rndSequence2 = bytearray(os.urandom(64))

    # generate hashes from byes sequences
    firstHash = hashlib.sha256(rndSequence1)
    firstDig = firstHash.hexdigest()
    secHash = hashlib.sha256(rndSequence2)
    secDig = secHash.hexdigest()
    firstPrefix = firstDig[:4]
    secPrefix = secDig[:4]

    if prefComparator.comp16bit(firstDig, secDig):
        print('Rounds till collision: {}'.format(loopCount))
        print(firstDig)
        print(secDig)
        print(firstPrefix)
        print(secPrefix)
        loopFlag = False

    else:
        loopCount += 1


print('collider finished!')