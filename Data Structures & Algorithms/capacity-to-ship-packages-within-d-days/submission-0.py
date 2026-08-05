class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        maximum_weights = sum(weights)
        min_weight = max(weights)
        best = maximum_weights
        while min_weight <= maximum_weights:
            middle = (maximum_weights + min_weight) // 2
            works = 1
            curr = 0
            day = 1
            for weight in weights:
                curr += weight
                if curr > middle:
                    day += 1
                    curr = weight
                    if day > days:
                        works = 0
                        break
                    continue
            if works == 1:
                best = middle
                maximum_weights = middle - 1
            else:
                min_weight = middle + 1
        return best

            