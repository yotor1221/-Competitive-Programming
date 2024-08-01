class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            j = i + 1
            if nums[i] == nums[j]:
                nums[i] *= 2
                nums[j] = 0
        
        seek = 0
        hold = 0
        while hold < len(nums):
            if nums[hold] != 0:
                nums[seek],nums[hold] = nums[hold],nums[seek]
                seek += 1
            hold += 1
        return nums
