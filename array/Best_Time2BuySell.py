from typing import List


class solution:
   def maxProfit(self,prices:List[int])->int :
      buy_mini = prices[0]
      profit_max = 0

      for price in prices:
        buy_mini = min(price,buy_mini)
        profit_max = max(profit_max, price- buy_mini)
        
      return profit_max
      
obj = solution()
print(obj.maxProfit([7,1,5,3,6,4]))
