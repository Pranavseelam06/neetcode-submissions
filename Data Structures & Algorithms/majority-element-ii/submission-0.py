class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        divide = len(nums) / 3
        unique = set()
        numbers = []
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1
            unique.add(nums[i])
        for num in unique:
            if count.get(num) > divide:
                numbers.append(num)
        return numbers
                