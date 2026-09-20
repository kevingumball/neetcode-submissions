class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        cur = [0] * len(triplets[0])

        for i in range(len(triplets)):
            status = True
            for j in range(len(triplets[0])):
                if triplets[i][j] > target[j]:
                    status = False
                    break
            if status:
                for j in range(len(triplets[0])):
                    cur[j] = max(cur[j], triplets[i][j])
        return cur == target
            
            
                

        