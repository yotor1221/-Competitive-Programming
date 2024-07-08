class Solution:
    def similarPairs(self, words: List[str]) -> int:
        char_set_count = defaultdict(int)
    
        for word in words:
            char_set = frozenset(word)
            char_set_count[char_set] += 1
        
        count = 0
        for freq in char_set_count.values():
            if freq > 1:
                count += (freq * (freq - 1)) // 2
                
        return count
