import heapq

class Solution(object):
    def getOrder(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: List[int]
        """
        # append original index
        for i, task in enumerate(tasks):
            task.append(i)  # task = [enqueueTime, processingTime, index]

        # sort by enqueueTime
        tasks.sort(key=lambda x: x[0])

        res = []
        minHeap = []
        time = tasks[0][0]
        i = 0
        n = len(tasks)

        while minHeap or i < n:
            # push all tasks that have become available
            while i < n and tasks[i][0] <= time:
                enqueueTime, procTime, idx = tasks[i]
                heapq.heappush(minHeap, (procTime, idx))
                i += 1

            if not minHeap:
                # jump time to the next task's enqueueTime, not procTime
                time = tasks[i][0]
                continue

            procTime, idx = heapq.heappop(minHeap)
            time += procTime
            res.append(idx)

        return res
