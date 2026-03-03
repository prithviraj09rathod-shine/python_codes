
def k_largest_elements(arr,k):
    k_largest_elements = []
    if k<0 or k> len(arr):
        return None  # Invalid k value
    #sorted_arr = sorted(arr, reverse=True) #descending order to get largest elements first
    #return sorted_arr[:k]
    for num in range(k): #range(k) to repeat k times
        print(f"Iteration: {num+1} out of k :{k}")
        max_elem = arr[0]
        for i in range(1, len(arr)):
            if arr[i] > max_elem:
                max_elem = arr[i]
        arr.remove(max_elem)
        k_largest_elements.append(max_elem)
    return k_largest_elements


print(k_largest_elements([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], 3)) # Output: [9, 6, 5]
print(k_largest_elements([10, 20, 20, 30], 2))  # Output: [30, 20]