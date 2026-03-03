""" from collections import Counter as counter 

def du_index(array):
	dup_index = []
	freq = counter(array)
	print(freq)
	

	for i,v in freq.items():
		if len(freq.items) > 1:
		#if len()v > 1:
			dup_index.append(i)
			print("Duplicate element:", i, "found at indices:", [index for index, value in enumerate(array) if value == i])
		else:
			pass
	return dup_index

array = [1,2,3,4,3,2,5,6,7,8,9,1]
print(du_index(array)) """


def find_duplicates_with_indices(lst):
    """
    Find duplicates in a list and return a dictionary
    mapping each duplicate value to the list of indices
    where it occurs.
    """
    seen = {}
    duplicates = {}

    for idx, val in enumerate(lst):
        if val in seen:
            # Already seen → add to duplicates
            print(f" If value:{val} in Seen",seen)
            if val not in duplicates:
                duplicates[val] = [seen[val]]  # include first occurrence
                print("stepwise duplicates",duplicates)
            duplicates[val].append(idx)
            print("Duplicates so far after appending",duplicates)
        else:
            # First time seeing this value
            print("First time Seen so far",seen)
            seen[val] = idx
            

    return duplicates


# Example usage
data = [10,40, 10, 20, 30, 10, 40, 20, 50, 10]
result = find_duplicates_with_indices(data)

print("Duplicates with indices:", result)

#find find_duplicates_with_indices
def find_duplicates_with_indices(lst):
    """
    Find duplicates in a list and return a dictionary
    mapping each duplicate value to the list of indices
    where it occurs.
    """

    duplicates = {}
    for idx, val in enumerate(lst):
        if lst.count(val) > 1:
            if val not in duplicates:
                duplicates[val] = [i for i, x in enumerate(lst) if x == val]
                print("duplicates", duplicates)
    return duplicates   

# Example usage
data = [10, 20, 30, 10, 40, 20, 50, 10]
#result = find_duplicates_with_indices(data)
#print("Duplicates with indices:", result)
#Output: Duplicates with indices: {10: [0, 3, 7], 20: [1, 5]}

