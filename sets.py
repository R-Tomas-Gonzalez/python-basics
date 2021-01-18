#sets are unordered collections of unique objects or dictionaries?
#Sets are great for having multiple outputs and comparing them

# my_set = {1,2,3,4,5,5} # => {1,2,3,4,5}
# my_set.add(100) #=> {1,2,3,4,5,100}
# my_set.add(2) #=> {1,2,3,4,5,100}

# print(my_set)

# #return a list or collection with unique items. Convert it into a set

# my_list = [1,2,3,4,5,5]

# print(set(my_list)) #{1,2,3,4,5}

#set objects does not support index. We must use value in my_set

# main set functions
# .difference()
# .discard()
# .difference_update()
# .intersection()
# .isdisjoint()
# .issubset()
# .issuperset()
# .union()

my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}

# .difference()
# returns the items that only exist in my_set and not in your_set
# my_set.difference(your_set) #=> this method returns in my_set compared to your_set
# print(my_set)

# .discard()
# discards a value in the set that you specify in the argument
# my_set.discard(3) => {1,2,4,5}
# print(my_set)

# .difference_update()
# removes the items that exist in both sets
# my_set.difference_update(your_set) #=> {1,2,3}
# print(my_set) 

# .intersection()
# gives the commonalities between two sets
# print(my_set.intersection(your_set)) #=>{4,5}
# shorthand
# print(my_set & your_set) #=>{4,5}

# .isdisjoint()
# returns a boolean whether or not two sets have anything in common. False if not, True if so.
# print(my_set.isdisjoint(your_set)) => false

# .union()
# adds one set to another (without commonalities)
# print(my_set.union(your_set)) #{1,2,3,4,5,6,7,8,9,10}
# shorthand
# print(my_set | your_set) #{1,2,3,4,5,6,7,8,9,10}

# .issubset()
# returns a boolean if the entirety of one set is within another set
# print(my_set.issubset(your_set)) #=> false
#if
my_set = {4,5}
your_set = {4,5,6,7,8,9,10}
# print(my_set.issubset(your_set)) #=> true

# .issuperset()
print(my_set.issuperset(your_set)) #=> false
print(your_set.issuperset(my_set)) #=> true