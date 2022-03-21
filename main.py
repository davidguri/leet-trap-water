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
