class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        store = set()
        store.add(0)

        total = sum(nums)
        if total % 2:
            return False
        half = total // 2
        


        for num in nums:
            new_store = store.copy()
            for d in store:
                item = num + d
                if item == half:
                    return True
                new_store.add(item)
            store = new_store
        
        return False