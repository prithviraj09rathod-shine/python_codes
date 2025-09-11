#https://medium.com/@Isidro/coding-journey-solving-150-leetcode-problems-410f835fea32
# Function to find the maximum number in an array
# The previous code can be improved by reducing the checks to 1 in the loop
#remember this
def find_max_number2(arr):
    if not arr:
        return None
    result = arr[0]
    for num in arr[1:]:
        # 1 check in the loop
        if num > result:
            result = num
    return result


# Another alternative if is initialize the code the the inf values
def find_max_number3(arr):
    if not arr:
        return None
    result = float('-inf')
    for num in arr:
        # 1 check in the loop
        if num > result:
            result = num
    return result

# Example usage:
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(find_max_number2(arr))  # Output: 9
print(find_max_number3(arr))  # Output: 9