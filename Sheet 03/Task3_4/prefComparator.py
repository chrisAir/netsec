def comp4bit(sequ1, sequ2):
    bitSequ1 = bin(int(sequ1, base=16)).lstrip('0b')[:4]
    bitSequ2 = bin(int(sequ2, base=16)).lstrip('0b')[:4]

    return bitSequ1 == bitSequ2


# this is redundant as we could just compare the first byte but for consistency's sake this method is created
def comp8bit(sequ1, sequ2):
    bitSequ1 = bin(int(sequ1, base=16)).lstrip('0b')[:8]
    bitSequ2 = bin(int(sequ2, base=16)).lstrip('0b')[:8]

    return bitSequ1 == bitSequ2


def comp12bit(sequ1, sequ2):
    bitSequ1 = bin(int(sequ1, base=16)).lstrip('0b')[:12]
    bitSequ2 = bin(int(sequ2, base=16)).lstrip('0b')[:12]

    return bitSequ1 == bitSequ2


# this is redundant as we could just compare the first two bytes but for consistency's sake this method is created
def comp16bit(sequ1, sequ2):
    bitSequ1 = bin(int(sequ1, base=16)).lstrip('0b')[:16]
    bitSequ2 = bin(int(sequ2, base=16)).lstrip('0b')[:16]

    return bitSequ1 == bitSequ2


def comp20bit(sequ1, sequ2):
    bitSequ1 = bin(int(sequ1, base=16)).lstrip('0b')[:20]
    bitSequ2 = bin(int(sequ2, base=16)).lstrip('0b')[:20]

    return bitSequ1 == bitSequ2
