class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
                # we check for all solutions
            if nums[i] > 0:
                break
            left = i + 1
            right = len(nums) -1 
            target = -nums[i]
            while left < right:
                if target > (nums[left] + nums[right]):
                    left = left + 1
                    continue
                if target < (nums[left] + nums[right]):
                    right = right - 1        
                    continue
                if target == (nums[left] + nums[right]):
                    ans.append([nums[i],nums[left],nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return ans     