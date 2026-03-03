
#finf unique elements/remove duplicates in a list without using functions
def removeDuplicates_fun(list1):
    unique_list = []
    for num in list1:
            if num not in unique_list:
                unique_list.append(num)
    return unique_list

def min_fun(list1):
    min = list1[0]
    for i in range(1, len(list1)):
        if list1[i] < min:
            min = list1[i]
    return min

def max_fun(list1):
    max = list1[0]
    for i in range(1, len(list1)):
        if list1[i] > max:
            max = list1[i]
    return max
    
def sort_list_func(list1):
    sorted_list = []

    while list1:
        min =list1[0]
        for i in range(1, len(list1)):
            if list1[i] < min:
                min = list1[i]
        sorted_list.append(min)
        list1.remove(min)
    return sorted_list

def duplicate_count(list1):
    count_dict = {}
    for num in list1:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    return count_dict

def dup_dict_indexfun(list1):
    dupdict_withIndex = {}
    for i, num in enumerate(list1):
        if list1.count(num) > 1:
            if num not in dupdict_withIndex:
                #or only this line sufficeint to capture all the duplicates for list comprehension and does not need if else block aswell
                #dupdict_withIndex[num] = [i for i,x in enumerate(list1) if x==num ]
                dupdict_withIndex[num] = [i]              
            else:
                dupdict_withIndex[num].append(i)
    return dupdict_withIndex

def dupDict_fun(list1):
    #count_dict = duplicate_count(list1)
    count_dict = {}
    dup_dict = {}
    for num in list1:
        if num in count_dict:
            count_dict[num] += 1
            #print(count_dict)
            dup_dict = {key: value for key, value in count_dict.items() if value > 1}
        else:
            count_dict[num] = 1
    
    return dup_dict

#shortest solution to find dupcates with indexes without using count dictionary
def dupDict_index_wocount(list1):
    dup_dict_index = {} # to store indices of duplicates
    for index, num in enumerate(list1):
        if num in dup_dict_index:
            dup_dict_index[num].append(index)
        else:
            dup_dict_index[num] = [index]

    # Uinsg list comprehension to Filter out entries that are not duplicates 
    dup_dict_index = {key: value for key, value in dup_dict_index.items() if len(value) > 1}
    return dup_dict_index

def dupDict_index_wocount_v2(list1):
    dup_dict_index = {} # to store indices of duplicates
    for index, num in enumerate(list1):
        #if list1.count(num) > 1:
            if num in dup_dict_index:
                dup_dict_index[num].append(index)
            else:
                dup_dict_index[num] = [index]

    # Filter out entries that are not duplicates
    result = {}
    for key, value in dup_dict_index.items():
        if len(value) > 1:
            result[key] = value
    print("result:", result)
    return result

def dupDict_index_fun(list1):
    count_dict = {} # to count occurrences
    dup_dict_index = {} # to store indices of duplicates
    for index, num in enumerate(list1):
        if num in count_dict:
            count_dict[num] += 1
            if num in dup_dict_index:
                dup_dict_index[num].append(index)
            else:
                dup_dict_index[num] = [index]
        else:
            count_dict[num] = 1

    return dup_dict_index


num = [1, 3, 2, 3, 4, 5, 1, 2, 3]
print("Original List:", num)
#print(min_fun(num))
#print(max_fun(num))
#print(removeDuplicates_fun(num))
#print(sort_list_func(num))
#sorted_array = sort_list_func(num)
#print(count_dict_fun(num)) # {1: 2, 3: 3, 2: 2, 4: 1, 5: 1}
#print(dupDict_fun(num))  # {1: 2, 3: 3, 2: 2}
#print(dupDict_index_fun(num))
#print(dupDict_index_wocount(num))
#print(dupDict_index_wocount_v2(num))
print(dup_dict_indexfun(num))





