#*arguments()-> * is used to unpack the elements
'''a=[1,2,3,4,5,6]
print(a)
print(*a)

b=(3,4,5,6,7)
print(b)
print(*b)

c={3,7,9,11,13}
print(*c)

d={"name":"pooja","year":2024,"month":11}
print(*d)

a,b,c=1,2,3
print(a)
print(b)
print(c)

a="codegnan"
print(a)
print(*a)


*a,b,c=1,2,3,4,5,6,7,8,9,10,11
print(*a)
print(b)
print(c)

a,b,c="codegnan"
print(a)
print(b)
print(c)'''

'''a,b,c="cod"
print(a)
print(b)
print(c)'''

#variable length arguments
#we can define any  no of arguments it will automatically stores in tuple we use * arguments
'''
def check(*a):
    print(a)
    print(type(a))
check()
check(2,3,4,5,6)
b=[6,7,8,9,10]
check(*b)
c={4,2,9,1,0}
check(*c)
d={"year":2024,"month":11}
check(*d)'''

'''def check1(*a):
    d=1#creating a variable
    print(a)
    print(type(a))
    for i in a:
        if type(i)==float or type(i)==int:
            d=d+i
            print(d)
        
check1()
check1(2,3,4,5,6)
check1(1,2,3,4.2,5.3,6.3)
check1(2,4,6,8,2.2,3.4,"pooja")'''


def check1(*a):
    d=1#creating a variable
    print(a)
    print(type(a))
    for i in a:
        if type(i) in (int,float):
            d=d+i
            print(d)
        
check1()
check1(2,3,4,5,6)
check1(1,2,3,4.2,5.3,6.3)
check1(2,4,6,8,2.2,3.4,"pooja")


