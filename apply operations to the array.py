class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            j = i + 1
            if nums[i] == nums[j]:
                nums[i] *= 2
                nums[j] = 0
        
        value = []
        zeros = 0
        for num in nums:
            if num != 0:
                value.append(num)
            else:
                zeros += 1
        
        value.extend([0] * zeros)
        return value
