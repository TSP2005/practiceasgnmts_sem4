list=[1,2,8,4,8,6,7,8,9,0]
c=int(input("Enter a number:" ))
l=[]
count=0
for i in range(len(list)):
    if c==list[i]:
        l.append(i+1)
        count+=1
print("the element ",c," repeated ",count," times")
print("The element occured in positions",l )