#list comprehension
list1 = [x**2 for x in range(1,11)]
print(list1)

mult_3_table = [x for x in range(1, 31) if x%3==0]
print(mult_3_table)

even_numbers = [x for x in range(1, 21) if x%2==0]
print(even_numbers)

#flatten a list of lists using 2 for loops in list comprehension
list_of_lists = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flatteened_list = [item for sublist in list_of_lists for item in sublist]
print(flatteened_list)

#matrix calculation using list comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transposed_matrix)

#or normal way
transposed = []
for i in range(len(matrix[0])):
    new_row = []
    for row in matrix:
        new_row.append(row[i])
    transposed.append(new_row)

print(transposed)

#shortest and best way using buildt in function
transposed_mat = list(zip(*matrix))
print("uising zip function")
print(transposed_mat)