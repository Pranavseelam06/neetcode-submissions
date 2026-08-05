class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_product = []
        r_product = []
        curr = 1
        for num in nums:
            l_product.append(curr)
            curr *= num
        curr = 1
        for num in reversed(nums):
            r_product.append(curr)
            curr *= num
        print(l_product)
        print(r_product)
        answer = []
        for i in range(len(nums)):
            answer.append(l_product[i] * r_product[len(r_product) - 1 -i])
        return answer