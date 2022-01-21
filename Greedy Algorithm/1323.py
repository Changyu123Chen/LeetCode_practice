class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        num1 = str(num)
        num1 = list(num1)
        for i in range(len(num1)):
            if(num1[i] == '6'):
                num1[i] = '9'
                num1 = ''.join(num1)
                
                break
        num1 = ''.join(num1)
        num = int(num1)
        return num
