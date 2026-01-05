class Solution:
    def reorganizeString(self, s: str) -> str:
        # STORE by freq

        # each char is added, by most freq

        count = Counter(s)
        maxHeap = []

        for c, cnt in count.items():
            print(cnt, c)
            maxHeap.append((-cnt, c))

        heapq.heapify(maxHeap)

        # now we do our operations
        # we add most freq
        # but we skip prev most freq so we dont do two in a row
        prev = None
        res = ""
        # a: 2
        # b: 1
        # ab
        # 1 a prev

        while maxHeap or prev:

            if not maxHeap and prev:
                return ""
            cnt, c = heapq.heappop(maxHeap)
            
            cnt += 1

            res += c
            
            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            if cnt < 0:
                prev = (cnt, c)

        return res
            
            