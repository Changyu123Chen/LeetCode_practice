class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        count_R = 0
        count_L = 0
        number = 0

        for i in range (n):
            if (s[i] == 'R'):
                count_R += 1
            else:
                count_L += 1
            if(count_R == count_L):
                number += 1
                count_L = count_R =0
        
        return number
