class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        heap = [-cnt for cnt in counts.values()]
        heapq.heapify(heap)
        
        queue = deque()
        time = 0
        while queue or heap:
            time += 1
            if heap:
                count = heapq.heappop(heap) + 1
                if count != 0:
                    queue.append([count,time + n])
            if queue:
                if queue and queue[0][1] == time:
                    heapq.heappush(heap, queue.popleft()[0])
        return time   
        