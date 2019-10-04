favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

print("Sarah's favorite language is " + favorite_languages['sarah'].title() + ".")

for key, value in favorite_languages.items():
    print("\nKey: " + key)
    print("Value: " + value)

myList=['spam','huevos','bacon','loaf']
s = '\n'
#print '\n' .join(myList)
print (s.join(myList))