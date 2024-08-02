person = dict(first_name='John', last_name='Doe', age=25, favorite_colors=['blue', 'green'], active=True)
print(person)
print("keys: ")
for key in person.keys():
    print(key)
print("values: ")
for value in person.values():
    print(value)
second_key= list(person.keys())[1]
print("second key value: "+str(person[second_key]))
