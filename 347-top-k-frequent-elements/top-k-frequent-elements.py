class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # array nums
        # k most freq elements
        hashSet = defaultdict(int)
        for num in nums:
            hashSet[num] += 1
        
        sortedList = sorted(hashSet, key=lambda x: hashSet[x], reverse=True)

        finalList = []
        for i in range(k):
            finalList.append(sortedList.pop(0))

        return finalList

