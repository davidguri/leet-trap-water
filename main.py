class Solution:
    def trap(self, height: List[int]) -> int:
        
        water = 0
        
        def first(rng, condition = lambda x: True):
            for d in rng:
                if condition(d):
                    return d
        
        for i in range(len(height)):
            if height[i] == 0:
                continue
                
            result = first(height[(i + 1):], lambda d: d >= i)
            
            #water += height[i]        
        return water
    
    
    
    
    
    
# This is the right solution
class Solution:
    def trap(self, height: List[int]) -> int:
        
        left = 0
        right = len(height) - 1
        left_max = 0
        right_max = 0
        res = 0
        
        if len(height) <= 2:
            return 0
        
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    res += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    res += right_max - height[right]
                right -= 1
                
        return res
