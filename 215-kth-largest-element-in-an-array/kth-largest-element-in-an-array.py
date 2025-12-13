import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        minHeap = nums[:]
        heapq.heapify(minHeap)

        while len(minHeap) > k:
            heapq.heappop(minHeap)

        return minHeap[0]
