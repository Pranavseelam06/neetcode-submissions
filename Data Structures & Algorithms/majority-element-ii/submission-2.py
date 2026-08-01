class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cand_one = [-1,0]
        cand_two = [-1,0]
        divide = len(nums) / 3
        for i in range(len(nums)):
            if nums[i] == cand_one[0]:
                cand_one[1] += 1
            elif nums[i] == cand_two[0]:
                cand_two[1] += 1
            elif nums[i] != cand_one[0] and cand_one[1] == 0:
                cand_one[0] = nums[i]
                cand_one[1] = 1
            elif nums[i] != cand_two[0] and cand_two[1] == 0:
                cand_two[0] = nums[i]
                cand_two[1] = 1
            else:
                cand_two[1] -= 1
                cand_one[1] -= 1
        count_one = 0
        count_two = 0
        for num in nums:
            if num == cand_one[0]:
                count_one += 1
            if num == cand_two[0]:
                count_two += 1
        ans = []
        if count_one > divide:
            ans.append(cand_one[0])
        if count_two > divide and cand_two[0] not in ans:
            ans.append(cand_two[0])
        return ans

