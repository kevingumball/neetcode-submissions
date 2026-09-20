class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        store = {}
        minHeap = []

        for num in hand:
            store[num] = store.get(num, 0) + 1
        
        for key in store.keys():
            heapq.heappush(minHeap, key)
        
        while minHeap:
            first = minHeap[0]

            for i in range(first, first + groupSize):
                if i not in store:
                    return False
                store[i] -= 1
                if store[i] == 0:
                    if i != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)

        return True



        