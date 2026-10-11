class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        for i in range(len(heights)):
            start = i
            while stack and stack[-1][1] > heights[i]:
                index, hei = stack.pop()
                res = max(res, (i - index) * hei)
                start = index
            stack.append((start, heights[i]))
        
        while stack:
            index, hei = stack.pop()
            res = max(res, (len(heights) - index) * hei)
        return res 
        