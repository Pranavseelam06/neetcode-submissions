class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        def product(nums: List[int]) -> int:
            return math.prod(nums)
        answer = []
        for i in range(len(nums)):
            answer.append(product(nums[0:i] + nums[i + 1:]))
        return answer