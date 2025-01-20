var=lambda v1,v2,v3 : v1+v2+v3
print(var(1,2,3))

print('-'*30)

res=lambda v1,v2,v3:v1+v2
print(res(v1=2,v3=6,v2=4))

print('-'*30)

print((lambda v1,v2:v1*v2)(4,5))
