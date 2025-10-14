class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = list()
        for elem in nums:
            heapq.heappush(heap, -elem)
        
        for _ in range(1, k):
            heapq.heappop(heap)

        return -heapq.heappop(heap)
