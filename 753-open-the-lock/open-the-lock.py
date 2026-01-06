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
    
        visited = set()
        dead = set(deadends)
        amountMoves = 0

        if "0000" in dead:
            return -1

        while q:
            code, layer = q.popleft()
            if code == target:
                return layer

            # we generate 8 neighbors
            for i in range(4):
                # we are iterating through each string number in lock
                # and we increment and decrement each
                c = code[i]
                c1 = (int(c) + 1) % 10
                c2 = (int(c) - 1) % 10
                newCode1 = code[:i] + str(c1) + code[i+1:]
                newCode2 = code[:i] + str(c2) + code[i+1:]

                if newCode1 not in dead and newCode1 not in visited:
                    q.append((newCode1, layer+1))
                    visited.add(newCode1)
                if newCode2 not in dead and newCode2 not in visited:
                    q.append((newCode2, layer+1))
                    visited.add(newCode2)
        # 0000
        # 1000
        # 9000
        # 0100
        # 0900
                

        return -1

