l = input("enter the numbers separated by space: ")
string_l = l.split()
int_l = [int(x) for x in string_l]
print("the entered list is: ")
for i in int_l:
    print(i)
