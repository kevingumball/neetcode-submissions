class Solution:
    def trap(self, height: List[int]) -> int:
        fromleft = [0]
        fromright = [0]
        maxleft = 0
        maxright = 0
        res = 0
        for i in range(1, len(height)):
            maxleft = max(maxleft, height[i - 1])
            fromleft.append(maxleft)
        for i in range(len(height) - 2, -1, -1):
            maxright = max(maxright, height[i + 1])
            fromright.append(maxright)
        fromright.reverse()
        for i in range(len(height)):
            cur = min(fromleft[i], fromright[i]) - height[i]
            if cur > 0:
                res += cur
        return res
        