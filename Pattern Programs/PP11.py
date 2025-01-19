num=5
for line in range(1,num+1):
    for col in range(line):
        print(num+1-line,end=' ')
    print()

print('------------')

num=5
copy=1
for line in range(num,0,-1):
    for col in range(line):
        print(copy,end=' ')
    print()
    copy=copy+1
