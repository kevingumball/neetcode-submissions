from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = defaultdict(int)
        for i, n in enumerate(nums):
            store[n] = i

        for i, n in enumerate(nums):
            need = target - n
            if need in store and i != store[need]:
                return [i, store[need]] if i < store[need] else [store[need], i]
        