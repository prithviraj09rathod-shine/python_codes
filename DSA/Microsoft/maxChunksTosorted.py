""" Example 1:

Input: arr = [4,3,2,1,0]
Output: 1
Explanation:
Splitting into two or more chunks will not return the required result.
For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn't sorted.
Example 2:

Input: arr = [1,0,2,3,4]
Output: 4
Explanation:
We can split into two chunks, such as [1, 0], [2, 3, 4].
However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks possible.
  """
""" Code #1
Time complexity: O(n). Space complexity: O(1). """

from itertools import accumulate, count, starmap
from operator import eq
from typing import List


class Solution:
    def maxChunksToSorted(self, a: List[int]) -> int:
        return sum(starmap(eq,enumerate(accumulate(a,max))))


""" Code #2
Time complexity: O(n). Space complexity: O(1). """

class Solution:
    def maxChunksToSorted(self, a: List[int]) -> int:
        return sum(map(eq,accumulate(a,max),count(0)))

""" Code #3
Time complexity: O(n). Space complexity: O(1). """

class Solution:
    def maxChunksToSorted(self, a: List[int]) -> int:
        return sum(max(a[:i+1])==i for i in range(len(a)))


#neetcode
class solution:
    def maxChunksToSorted(self, arr:List[int]) -> int:
        curr_max = -1
        res = 0

        for i, n in enumerate(arr):
            curr_max = max(n, curr_max)

            if curr_max == i:
                res+=1
        return res
input = [1, 0, 2, 4, 3]
obj =solution()
print(obj.maxChunksToSorted(input))

##https://www.youtube.com/watch?v=r5-HS3HyjIE