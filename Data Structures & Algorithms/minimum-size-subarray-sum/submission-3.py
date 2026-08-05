class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_size = 100001
        left = 0
        total = 0
        for right in range(len(nums)):
            total += nums[right]
            while total >= target and right >= left:
                min_size = min(min_size, right - left + 1)
                total -= nums[left]
                left += 1
        if min_size == 100001:
            return 0
        return min_size