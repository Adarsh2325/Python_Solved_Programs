num=4
spaces=0
for line in range(num,0,-1):
    for sp in range(spaces):
        print(' ',end='  ')
    for st in range(line):
        print('*',end=' ')
    print()
    spaces=spaces+1
