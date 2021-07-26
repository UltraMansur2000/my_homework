import sys

with open('buys.txt', 'a', encoding='utf-8') as f:
    f.write(f'{sys.argv[1]}\n')
