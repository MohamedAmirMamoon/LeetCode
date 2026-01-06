class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        # 8 char long string
        # ACGT
        # startGene to a gen string endGene
        # one mutation is defined as one single char changed in a gene
        # one char change is one mutation
        # gene bank recording all valid gene mutations
        # a gene must be in bank for it to be valid
        # min paths to mutate from start to end gene
        # if none exists then return -1
        
        # we thing of it like a string
        # and we can iterate through each char by changing one at a time between the other three
        # if it exists in the bank then we can add it to queue until we reach end gene
        q = deque()
        q.append((startGene, 0))
        if startGene == endGene:
            return 0

        while q:
            gene, steps = q.popleft()
            # AACCGGTT
            if gene == endGene:
                return steps
            for i in range(len(gene)):
                for m in "ACGT":
                    newGene = gene[:i] + m + gene[i+1:]
                    if newGene in bank:
                        q.append((newGene, steps+1))
                        bank.remove(newGene)

        return -1