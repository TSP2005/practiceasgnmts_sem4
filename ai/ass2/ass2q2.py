n = int(input("Enter no.of characters to read:"))
f = open('example.txt','r')
c = f.read(n)
print("the ", n ," no.of characters in file is",c)