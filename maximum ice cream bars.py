class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort() 
        count = 0
        creams = 0

        for cost in costs:
            if creams + cost <= coins:
                creams += cost
                count += 1
            else:
                break
        
        return count
