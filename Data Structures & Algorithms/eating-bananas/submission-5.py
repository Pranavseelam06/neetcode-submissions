class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        max_speed = piles[-1]
        min_speed = 1
        best = max_speed
        min_count = 10000000
        while min_speed <= max_speed:
            middle = (min_speed + max_speed) // 2
            count = 0
            for pile in piles:
                count += (pile + middle - 1) // middle
            if count <= h:
                best = middle
                max_speed = middle - 1
            else:
                min_speed = middle + 1
        return best


