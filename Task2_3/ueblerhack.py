path = 'rfc3093.txt'

file = open(path, 'r')

for line in file:
    for word in line.split():
        print word


file.close()