import sys

with open('buys.txt', 'r', encoding='utf-8') as f:
    if len(sys.argv) == 1:
        print(f.read(),end='')
    else:
        for n, i in enumerate(f, 1):
            if len(sys.argv) == 2 and int(sys.argv[1]) - 1 == n:
                print(f.read().strip())
            elif len(sys.argv) == 3 and int(sys.argv[1]) - 1 == n:
                for m in range(int(sys.argv[2])-int(sys.argv[1])):
                    print(f.readline().strip())
