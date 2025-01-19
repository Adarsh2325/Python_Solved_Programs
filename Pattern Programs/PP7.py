num=4
spaces=num-1
for line in range(1,num*2,2):
    for sp in range(spaces):
        print(' ',end=' ')
    for st in range(line):
        print('*',end='')
    print()
    spaces=spaces-1

print('OR')

num=4
spaces=0
for line in range(num*2-1,0,-2):
    for sp in range(spaces):
        print(' ',end=' ')
    for st in range(line):
        print('*',end='')
    print()
    spaces=spaces+1

