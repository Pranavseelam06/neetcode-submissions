# 
#
#
#
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        removed = 0
        for i in range(len(nums) - removed):
            if nums[i - removed] == val:
                nums.remove(val)
                removed = removed + 1
            else:
                count = count + 1
        for i in range(removed):
            nums.append(None)
        return count