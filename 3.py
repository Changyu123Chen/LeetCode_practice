class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp = []
        maxs = 0
        for item in s:
            if item not in temp:
                temp.append(item)
            else:
                i = temp.index(item)
                temp = temp[i+1:]
                temp.append(item)
            maxs = max(len(temp), maxs)
        return maxs
                    

