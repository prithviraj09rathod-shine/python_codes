list1 = [1,2,3,4,5]
list2 = [2,6,3,7,5]


#common_elements = list(set(list1) & (set(list2)))
common_element = list(set(list1 & list2))
print("Common elements:", list(common_elements))