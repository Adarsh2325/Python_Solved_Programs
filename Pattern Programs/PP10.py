num=5
for line in range(1,num+1):
    for col in range(line):
        print(line,end=' ')
    print()

print('OR')

num=5
for line in range(num,0,-1):
    for col in range(line):
        print(line,end=' ')
    print()

