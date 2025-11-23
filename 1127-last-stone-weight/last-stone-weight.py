class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones=[-s for s in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            first=abs(heapq.heappop(stones))
            second=abs(heapq.heappop(stones))
            if first>second:
                new_stone=first-second
                heapq.heappush(stones,-new_stone)
        return -stones[0] if stones else 0        