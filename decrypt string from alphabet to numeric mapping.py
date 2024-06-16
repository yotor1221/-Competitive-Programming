class Solution:
    def freqAlphabets(self, s: str) -> str:
        dic_map = {str(i) : chr(96 + i) for i in range(1,10)}
        dic_map.update({str(i) + "#" : chr(96 + i) for i in range(10,27)})
        result = []
        
        i = 0
        while i < len(s):
            if i + 2 < len(s) and s[i+2] == "#":
                key = s[i:i + 2] + "#"
                result.append(dic_map[key])
                i += 3
            else:
                key = s[i]
                result.append(dic_map[key])
                i += 1

        return "".join(result)
