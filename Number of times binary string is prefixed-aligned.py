class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        max_flipped = 0
        steps = 0

        for i, flip in enumerate(flips):
            max_flipped = max(max_flipped, flip)
            if max_flipped == i + 1:
                steps += 1
                
        return steps
