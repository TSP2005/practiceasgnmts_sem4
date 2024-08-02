a=int(input("Enter size of list:"))
list1 = [int(input()) for i in range(a)]
list2 = [int(input()) for i in range(a)]
maxl=[]
for i in range(a):
    b=max(list1[i],list2[i])
    maxl.append(b)
print(maxl)