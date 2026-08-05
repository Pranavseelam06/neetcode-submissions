class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        current_sum = 0
        answer = 0
        dictionary = {}
        dictionary[0] = 1 # since if its 0 then its a answer
        for num in nums:
            current_sum += num
            answer += dictionary.get(current_sum - k, 0)
            dictionary[current_sum] = dictionary.get(current_sum, 0) + 1
        return answer
