class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
      
        for num in range(left,right+1):
            cov = any(start <= num <= end for start,end in ranges)

            if not cov:
                return False
        
        return True
