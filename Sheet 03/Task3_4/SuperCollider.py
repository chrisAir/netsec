import os
import hashlib
import prefComparator
import matplotlib.pyplot as plt

TAB_1 = '\t - '


def main():
    four = []
    eight = []
    twelve = []
    sixteen = []
    twenty = []
    for i in range(0, 5):
        four.append(calcCollision(4))
        eight.append(calcCollision(8))
        twelve.append(calcCollision(12))
        sixteen.append(calcCollision(16))
        twenty.append(calcCollision(20))

    average = [sum(four) / len(four), sum(eight) / len(eight), sum(twelve) / len(twelve), sum(sixteen) / len(sixteen),
               sum(twenty) / len(twenty)]

    print('4-bit prefix:')
    print(TAB_1 + 'collisions occured at {} repetitions with an average of {}'.format(four, average[0]))
    print('8-bit prefix:')
    print(TAB_1 + 'collisions occured at {} repetitions with an average of {}'.format(eight, average[1]))
    print('12-bit prefix:')
    print(TAB_1 + 'collisions occured at {} repetitions with an average of {}'.format(twelve, average[2]))
    print('16-bit prefix:')
    print(TAB_1 + 'collisions occured at {} repetitions with an average of {}'.format(sixteen, average[3]))
    print('20-bit prefix:')
    print(TAB_1 + 'collisions occured at {} repetitions with an average of {}'.format(twenty, average[4]))


    # plotting realized in python
    plt.plot([4, 4, 4, 4, 4], four, 'kx')
    plt.plot([8, 8, 8, 8, 8], eight, 'kx')
    plt.plot([12, 12, 12, 12, 12], twelve, 'kx')
    plt.plot([16, 16, 16, 16, 16], sixteen, 'kx')
    plt.plot([20, 20, 20, 20, 20], twenty, 'kx')
    plt.plot([4, 8, 12, 16, 20], average, 'ro-')
    plt.ylabel('collision occured')
    plt.xlabel('bit prefix')
    plt.show()


# helper method to calculate the amount of tries till a collision occurs
def calcCollision(bitLength):
    loopFlag = True
    loopCount = 1
    func = switcher[bitLength]
    while loopFlag:
        # generate two random byte sequences
        rndSequence1 = bytearray(os.urandom(64))
        rndSequence2 = bytearray(os.urandom(64))

        # generate hashes from byes sequences
        firstHash = hashlib.sha256(rndSequence1)
        firstDig = firstHash.hexdigest()
        secHash = hashlib.sha256(rndSequence2)
        secDig = secHash.hexdigest()

        if func(firstDig, secDig):
            loopFlag = False

        else:
            loopCount += 1

    return loopCount


switcher = {
    4: prefComparator.comp4bit,
    8: prefComparator.comp8bit,
    12: prefComparator.comp12bit,
    16: prefComparator.comp16bit,
    20: prefComparator.comp20bit,
}

main()
