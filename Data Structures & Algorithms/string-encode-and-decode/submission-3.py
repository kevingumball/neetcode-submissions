class Solution:

    def encode(self, strs: List[str]) -> str:
        mes = []
        for s in strs:
            n = len(s)
            mes.append(str(n))
            mes.append("#")
            mes.append(s)
        return "".join(mes)

    def decode(self, s: str) -> List[str]:
        res = []
        l = 0
        while l < len(s):
            j = l
            while s[j] != "#":
                j += 1
            num = int(s[l:j])
            res.append(s[j+1: j+1+num])
            l = j + 1 + num
        return res
