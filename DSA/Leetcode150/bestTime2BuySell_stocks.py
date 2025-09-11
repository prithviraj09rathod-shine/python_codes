#buy when very low 
#sell when very high
#therefore we can maximize the profit



from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]
        for p in prices:
            buy = min(buy,p)
            profit = max(profit, p-buy  )
        return profit
    
#Example usage:
obj = Solution()
print(obj.maxProfit([7,1,5,3,6,4])) #5
print(obj.maxProfit([1,2,3,4,5])) #4
