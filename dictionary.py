#Dictionary
#These are data structures and data types
#A dictionary is an unordered key-value pair

dictionary = {
  'a': 0,
  'b': 1
}

print(dictionary['b'])

#keys in dictionaries must be immutable
#keys in dictionaries must be unique

#get method
#checks the dictionary for the key you specify
print(dictionary.get('c')) #None
print(dictionary.get('a')) #0

#"getting" a new key if it doesn't exist and setting it to a default value

print(dictionary.get('c', 2)) #2

#assigning a new key-value pair
dictionary['c'] = 2
print(dictionary) #{'a': 0, 'b': 1, 'c': 2}

#or

dictionary.update({'d':3})
print(dictionary) #{'a': 0, 'b': 1, 'c': 2, 'd': 3}