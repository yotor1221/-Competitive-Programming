class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counter = {}
        
        for num in arr1:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        

        result = []
        for num in arr2:
            if num in counter:
                result.extend([num] * counter[num])
                del counter[num]  
        
      
        remaining = []
        for num in counter:
            remaining.extend([num] * counter[num])
        
        remaining.sort()
        
        result.extend(remaining)
        
        return result
