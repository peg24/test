'''
the clown ran after the car and the car ran into the tent and the tent fell down on the clown and the car 

'''


#string -> liste -> lager histogram

counts = dict()
print('Enter a line of text:')
line = input('')

words = line.split()

print('Words:', words)

print('Counting...')
for word in words:
    counts[word] = counts.get(word,0) + 1
print('Counts', counts)


'''
Even though dictionaries are not stored in order, we can write a for loop that goes through all the entries in a dictionary - actually it goes through all of the keys in the dictionary and looks up the values
'''
counts = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
for key in counts:
     print(key, counts[key])
 
# Iterasjon på to variable
jjj = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
for aaa,bbb in jjj.items() :
    print(aaa, bbb)



