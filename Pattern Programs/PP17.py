num=5
spaces=num-1
for sv in range(num,0,-1):
    for sp in range(spaces):
        print(' ',end=' ')
    for val in range(sv,6):
        print(val,end='')
    print()
    spaces=spaces-1
