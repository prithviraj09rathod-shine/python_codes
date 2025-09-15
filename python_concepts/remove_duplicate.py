list1 = [1,2,3,4,5,1,2,3]
list2 = [10, 100, 89, 78, 56, 10, 100, 89]

rm_duplicate = list(set(list1))
print(rm_duplicate)
#Output: [1, 2, 3, 4, 5] (order may vary)
rm_duplicate2 = list(set(list2))
print(rm_duplicate2)
#Output: [100, 10, 78, 89, 56] (order may vary)
#Note: Using set() removes duplicates but does not preserve the original order of elements.