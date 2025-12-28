class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # 10 slots
        # initially starts at 0000
        # 0200

        # given list of deadends
        # you cant go down that path anymore
        # given target code
        # return min total number of turns required to open the lock

        # bfs bc min number of turns
        

        q = deque()

        # we will flip throguh each digit and go level by level order to find a shortest distance
        # we will make one turn at a time and add to queue
        q.append(("0000", 0))
        amountMoves = 0
        directions = [1, -1]
        visited = set()
        dead = set(deadends)

        if "0000" in dead:
            return -1

        while q:
            code, layer = q.popleft()
            if code == target:
                return layer

            # we generate 8 neighbors
            for i in range(4):
                for d in directions:
                    newDig = (int(code[i]) + d) % 10
                    newCode = code[:i] + str(newDig) + code[i+1:]
                    if newCode not in dead and newCode not in visited:
                        q.append((newCode, layer + 1))
                        visited.add(newCode)

        return -1

