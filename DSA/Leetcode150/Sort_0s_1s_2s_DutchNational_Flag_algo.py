
#Dutch National Flag algo
def dutch_national_flag(arr):
    low = mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  # arr[mid] == 2
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr

#normal way of counting
def sort_012(arr):
    count = {0: 0, 1: 0, 2: 0}

    # Count occurrences
    for num in arr:
        count[num] += 1

    # Overwrite array based on counts
    index = 0
    for num in [0, 1, 2]:
        for _ in range(count[num]):
            arr[index] = num
            index += 1

    return arr

#normal way of counting
from collections import Counter

def sort_012_counter(arr):
    count = dict(Counter(arr))
    print(count)

    # Overwrite array based on counts
    index = 0
    for num in [0, 1, 2]:
        for _ in range(count[num]):
            arr[index] = num
            index += 1

    return arr

arr = [2,0,2,1,1,0]
sorted_arr = dutch_national_flag(arr)
print("sorted array:", sorted_arr)
sorted_arr = sort_012_counter(arr)
print("sorted array:", sorted_arr)