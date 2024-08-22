class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        count = [0]*len(nums)
        for i in range(len(nums)):
            num = nums[i]
            for n in range(len(nums)):
                if nums[n] < num:
                    count[i] += 1
        return count
