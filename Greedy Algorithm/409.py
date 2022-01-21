class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = list(s)
        s.sort()
        i = 0
        tot = 0
        odd = 0
        num = 0
        
        while(i<len(s)):
            num = s.count(s[i])
            if num % 2== 0:
                tot += num
            
            else:
                tot += num-1
                odd = 1
            i += num
        
        return tot+odd
