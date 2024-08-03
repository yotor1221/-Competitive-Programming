class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        maximum = max(nums)
        count = [0] * (maximum + 1)
        for num in nums:
            count[num] += 1

        target = 0
        for index, value in enumerate(count):
            for i in range(value):
                nums[target] = index
                target += 1
