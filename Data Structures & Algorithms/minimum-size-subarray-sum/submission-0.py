class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        total = 0
        size = 1000000
        for i in range(len(nums)):
            total += nums[i]
            while l <= i and total >= target:
                if i - l + 1 < size:
                    size = (i - l) + 1 
                total = total - nums[l]
                l += 1
        if size == 1000000:
            return 0
        return size
            

            