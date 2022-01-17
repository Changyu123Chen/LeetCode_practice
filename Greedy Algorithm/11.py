class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        volume = 0
        while (left < right):
            volume1 = min(height[left], height[right]) * (right-left)
            volume = max(volume, volume1)
            if(height[left] < height[right]):
                left += 1
            else:
                right -= 1
        return volume
            
        
        
        
                
        
