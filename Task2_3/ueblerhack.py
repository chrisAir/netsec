from aprmd5 import password_validate

path = 'rfc3093.txt'
hash = "$apr1$/pE9u4cQ$ZfQfXfZ8NWh2gfFpIx22T0"

file = open(path, 'r')

removechars = ['.', ',', '[', ']', '(', ')', '{', '}', '"']
sc = set(removechars)

for line in file:
    for word in line.split():
        word = ''.join([c for c in word if c not in sc])
        if password_validate(word, hash):
            print ("this is the password: "+word)


file.close()