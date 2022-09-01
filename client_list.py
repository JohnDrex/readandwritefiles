def main():
    infile = open('clients.txt', 'r')

    i = 0
    for line in infile:
        print(i, '. ', line.rstrip('\n'), sep='')
        i += 1

main()