class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}

        for i, n in enumerate(nums):
            need = target - n
            if need in store:
                return [store[need], i]
            store[n] = i
            
        