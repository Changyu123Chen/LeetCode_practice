class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        candy = [1] * len(ratings)
        for i in range (1, len(ratings)):
            if(ratings[i] > ratings[i-1]):
                candy[i] = candy[i-1] + 1
        
        for j in range (len(ratings)-1, 0, -1):
            if (ratings[j-1] > ratings[j]):
                candy[j-1] = max(candy[j-1], candy[j]+1)
            
        return sum(candy)
        
