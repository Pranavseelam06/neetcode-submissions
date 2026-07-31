class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        highest = 0
        highest_count = 0
        num_count = {}
        for i in range(len(nums)):
            count = 0
            if nums[i] in num_count:
                num_count[nums[i]] += 1
                count = num_count[nums[i]]
            else:
                num_count[nums[i]] = 1
                count = 1
            if count > highest_count:
                highest = nums[i]
                highest_count = count
        return highest