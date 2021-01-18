#lists are pretty much arrays with some differences
#collections of items

#lists are Data Structures

li = [1,2,3,4,5]
li2 = ['a', 'b', 'c']
li3 = [1,2,'a',True]

# Data Structures - A way for us to organize info and data

#Shopping Cart Example

shopping_cart = [
  'notebooks', 
  'sunglasses', 
  'toys', 
  'grapes'
]

#Accessing Cart

#prints the entire shopping_cart
print(shopping_cart)

#prints the first index of the shopping_cart
print(shopping_cart[0])

#prints the last index of the shopping_cart
print(shopping_cart[len(shopping_cart)-1])

#changing the original arrays
# shopping_cart[0] = 'laptop'
print(shopping_cart)

#list slicing creates a copy of the original list
new_cart = shopping_cart[:]
new_cart[0] = 'laptop'
print(new_cart)

##################################################

#Actions

#finding the length of a list

basket = [1,2,3,4,5]

# print(len(basket)) #5

#METHODS

#ADDING to lists

#append method
#adds to the end of the list
basket.append(100)
# print(basket)

#insert method
#inserts into list where you specify, in this case, inserts 100 into index 1
# basket.insert(1, 100)
# print(basket)

#extending a list
#takes an iterable(another list) and appends it to the end
# basket.extend([100,101])
# print(basket)

#REMOVING from lists

#pop method
#removes the last index of the list and returns the value
# basket.pop()
# #you can specify an index to remove in the index
# basket.pop(0)
# print(basket)

#remove method
#you specify what value you'd like to remove
# basket.remove(1)
# print(basket)

#clear method
#clears out the list
basket.clear()
print(basket)

##################################################

#Methods

basket = ['a','b','c','d','e']

#index method
#provides the index of the value you specify
#you can also specify which indexes to search(start and stop) within the list
# print(basket.index('c',0,4))

#in keyword
# print('b' in basket) #true
# print('x' in basket) #false

#count method
#counts how many times a value occurs in a list
# print(basket.count('d'))

#sort method
#sorts the list from a-z and modifies the original array
# basket = ['x', 'b', 'a', 'c', 'd', 'e', 'd']
# basket.sort()
# print(basket)

#sorted method
#sorts the list from a-z but makes a copy and doesn't modify the original
# basket = ['x', 'b', 'a', 'c', 'd', 'e', 'd']
# new_basket = sorted(basket)
# print('the new basket:', new_basket) 
# print('the original basket:', basket)

#reverse method
#reverses the list without sorting
# basket.reverse()
# print(basket)

#join method
#joins the values in a list to make a string
# new_sentence = ' '.join(['hello', 'my', 'age', 'is', str(28)])
# print(new_sentence)

#list unpacking
#this allows you to assign a variable to individual values in a list. you can also section off certain groups of values

a,b,c,*other,d,e = [1,2,3,4,5,6,7,8,9]

print(a,b,c,other,d,e)
