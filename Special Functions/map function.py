def number(n):
    if n%2==0:
        return 'even'
    return 'odd'
print(list(map(number,[11,12,13,14,15])))

print('-'*20,'Using Lambda in map Func','-'*20)

print(list(map(lambda ch : ch*3,'abcd')))

print('-'*20)

def conc(ch1,ch2):
    return ch1+ch2
print(list(map(conc,'abcd','pqrs')))

print('-'*20)

print(list(map(lambda ch1,ch2:ch1+ch2,'abcd','pqrs')))

print('-'*20)

def prime(num):
    for den in range(2,num//2+1):
        if num%den==0:
            return 'Not prime num'
        return 'Prime Num'
print(list(map(prime,(21,14,23,5))))
