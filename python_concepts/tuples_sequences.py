 #
#set comprehension
set_comprehension_odd_values = {x for x in range(1, 21) if x % 2 != 0}
print(set_comprehension_odd_values)

###Dictionary
#dictionary comprehension
dict_compr = {x:x**2 for x in range(4)}
print(dict_compr)

#looping techniques in dictionary comprehension#
dict = {'a': 1, 'b': 2, 'c': 3}
squared_dict = {key: value**2 for key, value in dict.items()}
print(squared_dict)

#normal function for dictionary comprehension
for key, value in dict.items():
    dict[key] = value**2
print("Reshma this is normal function")
print(dict)

#building dictionary from sequences of key value pairs
keys = ['space', 'delete', 'resh', 'jani']
values = [1, 2, 3, 4]
list_to_dict_conv = {keys[i]: values[i] for i in range(len(keys))}  
#or using zip function
list_to_dict_conv = {k:v for k,v in zip(keys, values)}
print("Reshma this is building dictionary from sequences of key value pairs")
print(list_to_dict_conv)

#using dict function
#print(dict([('space':1),('delete':2),('resh':3),('jani':4)]))
"""Tuple comprehension doesn’t actually exist in Python.
If you write (x for x in range(5)), Python creates a generator, not a tuple.
- To make a tuple, you need to wrap a list comprehension in tuple(): """
#list comprehension inside tuple()
tuple_comp = tuple([x for x in range(5)])
print("Reshma this is tuple comprehension using list inside tuple()")
print(tuple_comp)

#tuple comprehension
tuple_compr = tuple(x**2 for x in range(5))
print("Really this is tuple comprehension?")
print(tuple_compr)
#tuple_updated = tuple_compr.append(6)  # This will raise an AttributeError since tuples are immutable   
#tuple_compr.add(7)  # This will raise an AttributeError since tuples do not have an add method
#print("After trying to update tuple comprehension")
#print(tuple_compr)
print(tuple_compr[2])  # Accessing element at index 2


#generator comprehension
generator_compr = (x**2 for x in range(5))