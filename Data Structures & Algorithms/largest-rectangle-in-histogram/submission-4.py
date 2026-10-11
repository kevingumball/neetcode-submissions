class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0

        for i in range(len(heights)):
            last = i
            while stack and stack[-1][1] > heights[i]:
                index, hei = stack.pop()
                res = max(res, (i - index) * hei)
                last = index
            stack.append((last, heights[i]))
        
        while stack:
            index, hei = stack.pop()
            res = max(res, (len(heights) - index) * hei)
        return res

        