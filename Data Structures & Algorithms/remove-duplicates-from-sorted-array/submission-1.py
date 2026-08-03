class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if (i + 1) < len(nums):
                while (i + 1) < len(nums) and nums[i + 1] == nums[i]:
                    nums.pop(i + 1)
        return len(nums)