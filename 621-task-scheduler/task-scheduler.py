class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # CPU tasks 
        # A to Z
        # min number of cpu intervals to complete all tasks
        # A A A B B B -> n=2
        # a gap of 2 intervals between 2 tasks with the same label
        # so i cant do A B (cant do b or a rn) so IDLE A B IDLE A B
        

        # we can track freq of tasks, so through an array 
        count = Counter(tasks)

        # then we can sort it using a maxHeap

        # algorithm
        # A A B B B C D 
        # find most freq, do that 
        # but we cant add back to heapq until the interval has passed
            # we can store in a map with cooldown interval
            # subtracting on each iteration of all of them
            # then if == 0 we add back to maxHeap
            # and we take most freq
            # otherwise if nothing in maxHeap take idle

        maxHeap = []
        for c, cnt in count.items():
            maxHeap.append((-cnt, c))

        heapq.heapify(maxHeap)

        coolDown = {}
        moves = 0
        idleMove = False
        while maxHeap or coolDown:
            moves += 1
        
            for key in list(coolDown):
                # subtract one or add to maxHeap
                coolDown[key] -= 1
                if coolDown[key] == 0:
                    heapq.heappush(maxHeap, key)
                    del coolDown[key]

            if maxHeap:
                cnt, c = heapq.heappop(maxHeap)
                cnt += 1
                if cnt < 0:
                    coolDown[(cnt, c)] = n + 1

        return moves


