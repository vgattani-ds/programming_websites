from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if not prices:
            return 0
        
        max_profit = 0
        current_price = prices[0]
        
        for price in prices[1:]:
            max_profit = max(max_profit, max_profit+price-current_price)
            current_price = price

        return max_profit
    
if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    print(Solution().maxProfit(prices))
    print(f"Correct Answer is: 7")