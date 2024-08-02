f2 = open('example.txt','a')
str = input("Enter some text to insert in the file in another line :")
f2.write("\n"+str)
f2 = open('example.txt','r')
for i in f2:
    print(i)
