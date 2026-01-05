class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # sorted in increasing order with ties

        # so we have two arrays
        # sorted
        # we add first elements in heap

        # while heap and k hasnt been reached
            # we check if i+1, j is in visited if not push to heap
            # same thing we check for i, j+1
            # then we -=k bc we have reduced the amount we need
            # then we go to next because we added 0,1 and 1,0 etc

        if not nums1 or not nums2 or k <= 0:
            return []

        minHeap = []

        heapq.heappush(minHeap, (nums1[0] + nums2[0], 0, 0))
        finalResult = []
        visited = set()

        while minHeap and k != 0:

            sum, i, j = heapq.heappop(minHeap)
            finalResult.append((nums1[i],nums2[j]))

            if i+1 < len(nums1) and (i+1, j) not in visited:
                heapq.heappush(minHeap, (nums1[i+1] + nums2[j], i+1, j))
                visited.add((i+1, j))
            if j+1 < len(nums2) and (i, j+1) not in visited:
                heapq.heappush(minHeap, (nums1[i] + nums2[j+1], i, j+1))
                visited.add((i, j+1))

            k-=1

        return finalResult




