import copy
list1 = [[1,2,3],[4,5,6]]

deepcopy_list = copy.deepcopy(list1)
shallowcopy_list = copy.copy(list1) 
#changing the original list, see in which copy it reflects
list1[0][0] = 10
print("Original List:", list1)  
'''it gets rerflected in shallow copy but not in deep copy
eg: if we change the first element of the original list from 1 to 10 then
Original List: [[10, 2, 3], [4, 5, 6]]'''
print("Shallow Copy List:", shallowcopy_list)
#Shallow Copy List: [[10, 2, 3], [4, 5, 6]]
print("Deep Copy List:", deepcopy_list)
#Deep Copy List: [[1, 2, 3], [4, 5, 6]]