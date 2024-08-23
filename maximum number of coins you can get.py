class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        n = len(piles) // 3
        max_coin = 0
        for i in range(n):
            max_coin += piles[2*i + 1]
        return max_coin
