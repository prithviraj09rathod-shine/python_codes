def second_largest(arr):
    if len(arr) < 2:
        return None  # Not enough elements for second largest
    first = second = float('-inf')
    for num in arr:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    return second

#print(second_largest([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])) # Output: 6
#print(second_largest([10, 20, 20, 30]))  # Output:


#tried and worked!! God Job Reshma
def SecLargest(arr):
    first = second = 0
    for i in range(len(arr)):
        if arr[i] > first:
            second = first
            first = arr[i]
        elif first > arr[i] and arr[i]> second:
            second = arr[i]
    return second if second != -float('inf') else None

print(SecLargest([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])) # Output: 6
#print(SecLargest([10, 20, 20, 30]))  # Output
