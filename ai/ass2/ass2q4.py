f = open('text.txt','w')
f.write("""A girl is playing there badminton.
The scenary is beautiful.
The birds are flying in the sky.
The sky is cloudy.
Alphabets consists of vowels and consonants.""")
f = open('text.txt','r')
c=0;
for i in f:
    if  i.strip()[0] != 'T':
        c+=1
print("No.of line without starting letter T is",c)