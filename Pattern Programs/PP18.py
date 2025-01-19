num=4
spaces=num-1
for ev in range(2,num*2,2):
    for sp in range(spaces):
        print(' ',end=' ')
    for val in range(1,ev):
        print(val,end='')
    print()
    spaces=spaces-1
