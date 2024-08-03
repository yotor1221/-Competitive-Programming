class Solution:
    def sortSentence(self, s: str) -> str:
        n = len(s)
        s = s.split()

        res = [""]*n
        for w in s:
            l = int(w[-1])-1
            res[l] = w[:-1]

        return " ".join(res).strip()
