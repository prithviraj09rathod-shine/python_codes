
def findMissingNUm(list1):
    # n is the expected maximum number (one missing from 1..n)
    n = len(list1) + 1
    missing_num = sum(range(1, n + 1)) - sum(list1) #range counts from 1 to n-1, so n+1 to include n
    print(missing_num)
    return missing_num

findMissingNUm([1, 2, 4, 6, 3, 7, 8])  # Output: 5
findMissingNUm([1, 2, 3, 5])  # Output: 4