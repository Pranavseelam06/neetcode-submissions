class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        # Now its 1,2,3,4,5,6
        l = 0
        r = len(people) - 1
        count = 0
        while l < r:
            print(people[r])
            if people[r] == limit:
                count += 1
                r -= 1
                continue
            if people[r] + people[l] <= limit:
                count += 1
                r -= 1
                l += 1
                continue
            if people[r] + people[l] > limit:
                count += 1
                r -= 1
                continue
        if r == l:
            count += 1

        return count
