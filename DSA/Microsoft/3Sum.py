from typing import List


class solution:
    #3 sum problem with best optimal approach using two pointers technique
    #O(n^2) time complexity
    def three_sum(self, arr:List[int]):
        arr.sort() #nlogn time
        res = []

        for i in range(len(arr)-2): #   O(n^2) time
            left=i+1
            right= len(arr)-1
            if i>0 and arr[i]==arr[i-1]:
                continue

            while left < right:
                sum = arr[left] + arr[right] + arr[i]
                if sum<0:
                    left+=1
                elif sum>0:
                    right-=1
                else:
                    res.append((arr[i], arr[left], arr[right]))
                    
                    #skipping duplicates
                    while left<right and arr[left]== arr[left+1]:
                        left+=1
                left +=1
                right -=1
        return res

#3sum problem using optimal approach with hashing
    def three_sum_hashing(self, arr:List[int])->List[List[int]]:
        #arr.sort()
        res = []
        n = len(arr)

        for i in range(n-2):
            if i > 0 and arr[i] == arr[i-1]:
                continue

            seen = set()
            for j in range(i+1, n):
                complement = -arr[i] - arr[j]
                if complement in seen:
                    triplet = (arr[i], complement, arr[j])
                    if triplet not in res:
                        res.append(triplet)
                seen.add(arr[j])

        return res


#3sum problem using optimal approach with hashing wihout sorting
    def three_sum_hashing_unsorted(self, arr:List[int])->List[List[int]]:
        res = set()
        n = len(arr)

        for i in range(n-2):
            seen = set()
            for j in range(i+1, n):
                complement = -arr[i] - arr[j]
                if complement in seen:
                    triplet = tuple(sorted((arr[i], complement, arr[j])))
                    res.add(triplet)
                seen.add(arr[j])

        return list(res)

obj = solution()
input = [-1,2,1,0,3,2,0]
print(obj.three_sum(input))
nums = [-1,2,1,0,3,2,9]
print(obj.three_sum(nums))
num1 = [-1, 0, 1, 2, -1, -4]
print(obj.three_sum(num1))