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

print(second_largest([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])) # Output: 6
print(second_largest([10, 20, 20, 30]))  # Output: