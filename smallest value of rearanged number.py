class Solution:
    def smallestNumber(self, num: int) -> int:

        if num < 0:
            num = -num
            num = list(str(num)) 
            num.sort(reverse=True)  
            return -int(''.join(num))

        
        num = list(str(num))
        num.sort()

        if num[0] != '0':
            return int("".join(num)) 

        for j in range(1, len(num)):
            if num[j] != '0':
                num[0], num[j] = num[j], num[0]
                break

        return int(''.join(num))
