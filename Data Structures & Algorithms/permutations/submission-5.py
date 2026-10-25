class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]

        for num in nums:
            new_perm = []
            for p in perms:
                for i in range(len(p)+1):
                    cur = p.copy()
                    cur.insert(i, num)
                    new_perm.append(cur.copy())
            perms = new_perm
        return perms
        