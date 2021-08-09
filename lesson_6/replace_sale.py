import sys
lines = []
with open('buys.txt','r+',encoding='utf-8') as f:
    for n,i in enumerate(f,1):
        if n == int(sys.argv[1]):
            lines.append(f'{sys.argv[2]}\n')
        else:
            lines.append(i)

with open('buys.txt','w',encoding='utf-8') as f:
    f.writelines(lines)
