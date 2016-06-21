#!/usr/bin/python
import hashlib

import sys

# key got from name2key on hellgate
key = b'6c82ad5b9a'
oPadBase = b'A5'
iPadBase = b'93'


# expected parameter is the path of the file which hash should be calculated


def main():
    if len(sys.argv) < 2:
        print "Please pass filepath as parameter"
        return
    path = sys.argv[1]

    # both pads are generated with the given key and the base values from the sheet
    iPad = buildPadWithKey(iPadBase, key)
    oPad = buildPadWithKey(oPadBase, key)
    sys.stdout.flush()

    # creating hash generator to be filled as soon as digest is available
    innerHash = hashlib.sha256()
    outerHash = hashlib.sha256()

    outerHash.update(oPad)
    innerHash.update(iPad)

    sourceFile = open(path, 'rb')
    # used to be a buffer implementation here but as the file is this small no buffer is needed
    innerHash.update(sourceFile.read())

    outerHash.update(innerHash.digest())
    finalHash = outerHash.hexdigest()

    print "the files hmac: \n" + finalHash


def padkey(baseKey, blocksize=64):
    # byte block size times 2 because here we need the amount of characters
    paddingGoal = blocksize * 2
    return baseKey.zfill(paddingGoal)


def expandpad(padBase):
    fullpad = bytes((x ^ padBase) for x in range(256))
    return fullpad


# snippet by Jason Scheirer @Stackoverflow
def repeat_to_length(string_to_expand, length):
    return (string_to_expand * ((length / len(string_to_expand)) + 1))[:length]


def xor_for_pad(padBase, key):
    intPadBase = int(padBase, 16)
    intKey = int(key, 16)
    finalPad = intPadBase ^ intKey
    return finalPad


def buildPadWithKey(padBase, key):
    expPadBase = repeat_to_length(padBase, 128)
    expKey = padkey(key)
    intPad = xor_for_pad(expPadBase, expKey)
    finalPad = "{:x}".format(intPad)
    return finalPad


if __name__ == '__main__':
    main()
