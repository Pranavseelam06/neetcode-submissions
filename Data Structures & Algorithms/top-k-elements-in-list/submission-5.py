class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        unique = set()
        for num in nums:
            count[num] = count.get(num,0) + 1
            unique.add(num)
        heap = []
        for num in unique:
            heapq.heappush(heap,(int(-1 * count[num]), num))
        answer = []
        for i in range(k):
            answer.append(heapq.heappop(heap)[1])
        return answer