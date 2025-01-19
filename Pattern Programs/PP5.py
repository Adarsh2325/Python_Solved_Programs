num=4
spaces=num-1
for line in range(1,num+1):
    for sp in range(spaces):
        print(' ',end=' ')
    for st in range(line):
        print('*',end=' ')
    print()
    spaces=spaces-1
