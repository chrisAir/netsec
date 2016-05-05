path = 'rfc3093.txt'

file = open(path, 'r')

removechars = ['.', ',', '[', ']', '(', ')', '{', '}', '"']
sc = set(removechars)

for line in file:
    for word in line.split():
        word = ''.join([c for c in word if c not in sc])
        print word


file.close()