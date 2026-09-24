class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # nums and k, return the k most frequent
        # we want to track the most frequent elements
        # figure out a way to count each element

        # maybe a heap?

        # with an array we iterate through
        # we can store a default dict and sort by values? and return the top 3 with an array?
        # O(n) by adding to map
        # instead of sort we just add by value wiht a hash
        # 1: 3 times, 2: 1 time(s), 3: 7 times

        # we can add to minheap and if already seen avoid it and do the next one
        heap = []
        heapq.heapify(heap)
        countNum = defaultdict(int)

        for num in nums:
            countNum[num] -= 1
            heapq.heappush(heap, [countNum[num], num])

        result = []
        
        alreadySeen = set()
        i = 0
        while i != k:
            num = -heapq.heappop(heap)[1]
            print(num)
            if num not in alreadySeen:
                result.append(-1*num)
                alreadySeen.add(num)
                i += 1
            

            

            
        return result