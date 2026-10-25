class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur = []

        def dfs(left, right):
            if left == right == n:
                res.append("".join(cur))
                return
            if left < n:
                cur.append("(")
                dfs(left + 1, right)
                cur.pop()
            if right < left:
                cur.append(")")
                dfs(left, right + 1)
                cur.pop()

        dfs(0, 0)
        return res
        