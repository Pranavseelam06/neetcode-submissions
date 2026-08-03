class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = set()
        count = 0
        answer = []
        for i in range(len(nums)):
            if nums[i] not in unique:
                unique.add(nums[i])
                answer.append(nums[i])
                count += 1
        nums[:] = answer
        return count