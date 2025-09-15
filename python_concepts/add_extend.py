fruits1 = ["apple", "banana", "cherry"]
fruits2 = ["orange", "mango", "grapes"]
fruits1.append("kiwi")
print(fruits1)
fruits1 = fruits1
fruits1.extend("kiwi")
print(fruits1)
print("=============Number LIST APPEND AND EXTEND=============")
#check how 2 lists are added using append() and extend()  
num1 = [1, 2, 3]
num2 = [4, 5, [8],6]
num1.append(num2)  #appends the entire list as a single element 
print(num1)
num3 = [1, 2, 3]
num4 = [4, 5,[8], 6]
num3.extend(num4)  #extends the list by appending elements from another list
print(num3)
print("=============fruits LIST APPEND AND EXTEND==")
fruits3 = ["apple", "banana", "mango"]
fruits4 = ["orange", "grapes"]
fruits3.append(fruits4)
print(fruits3)
fruits5 = ["apple", "banana", "mango"]
fruits6 = ["orange", "grapes"]
fruits5.extend(fruits6) 
print(fruits5)
print("=============TUPLE APPEND AND EXTEND=============")
#tuple does not support append and extend methods
tup1 = (1, 2, 3)
tup2 = (4, 5, 6)
#tup1.append(tup2)  #AttributeError: 'tuple' object has no attribute 'append'
#print(tup1)
#tup1.extend(tup2)  #AttributeError: 'tuple' object has no attribute 'extend'
#print(tup1)
print("=============DICTIONARY APPEND AND EXTEND=============")
#dictionary does not support append and extend methods
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
#dict1.append(dict2)  #AttributeError: 'dict' object has no attribute
#print(dict1)
#dict1.extend(dict2)  #AttributeError: 'dict' object has no attribute
#print(dict1)
print("=============SET APPEND AND EXTEND=============")
#set does not support append and extend methods
set1 = {1, 2, 3}
set2 = {4, 5, 6}
#set1.append(set2)  #AttributeError: 'set' object has no attribute '
#print(set1)
#set1.extend(set2)  #AttributeError: 'set' object has no attribute '
#print(set1)
print("=============STRING APPEND AND EXTEND=============")
#string does not support append and extend methods
str1 = "Hello"
str2 = " World"
#str1.append(str2)  #AttributeError: 'str' object has no attribute
#print(str1)
#str1.extend(str2)  #AttributeError: 'str' object has no attribute
#print(str1)
print("=============FROZENSET APPEND AND EXTEND=============")
#frozenset does not support append and extend methods
frozenset1 = frozenset([1, 2, 3])
frozenset2 = frozenset([4, 5, 6])
#frozenset1.append(frozenset2)  #AttributeError: 'frozenset' object has no attribute
#print(frozenset1)
#frozenset1.extend(frozenset2)  #AttributeError: 'frozenset' object has no attribute
#print(frozenset1)
print("=============BYTES APPEND AND EXTEND=============")
#bytes does not support append and extend methods
bytes1 = bytes([65, 66, 67])
bytes2 = bytes([68, 69, 70])
#bytes1.append(bytes2)  #AttributeError: 'bytes' object has no attribute
#print(bytes1)
#bytes1.extend(bytes2)  #AttributeError: 'bytes' object has no attribute
#print(bytes1)
print("=============BYTEARRAY APPEND AND EXTEND=============")
#bytearray supports append() but not extend()
bytearray1 = bytearray([65, 66, 67])
bytearray2 = bytearray([68, 69, 70])
bytearray1.append(68)  #appends a single byte (integer in range 0-255)
print(bytearray1)
#bytearray1.extend(bytearray2)  #AttributeError: 'bytearray' object has no attribute
#print(bytearray1)
print("=============MEMORYVIEW APPEND AND EXTEND=============")
#memoryview does not support append and extend methods
memoryview1 = memoryview(b'Hello')
memoryview2 = memoryview(b' World')
#memoryview1.append(memoryview2)  #AttributeError: 'memoryview' object
#print(memoryview1)
#memoryview1.extend(memoryview2)  #AttributeError: 'memoryview' object
#print(memoryview1)
print("=============OOPS CONCEPTS=============")




