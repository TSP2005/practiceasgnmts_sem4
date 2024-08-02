import sympy as sm
a=int(input("Enter size of list:"))
list = [int(input()) for i in range(a)]
p=0;
np=0;
o=0;
e=0;
def isEven(i):
    if i%2==0:
        return True
for i in list:
    if i>1:
        if sm.isprime(i):
            p+=1
        else:
            np+=1
    if i>0:
        if isEven(i):
            e+=1
        else:
            o+=1
print("The no.of prime,nonprime are ",p,np)
print("The no.of even,odd are ",e,o)
