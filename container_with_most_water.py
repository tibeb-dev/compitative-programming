class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxim = 0

        l = 0
        r = len(height)-1

        while(l<r):
            maxim = max(maxim,min(height[l],height[r])*(r-l))

            if height[l]<height[r]:
                l+=1
            else:
                r-=1

        return maxim        

    
#     [1,8,6,2,5,4,8,3,7]
#        l             r
    
#     max(1,min(8,49))
#     max =1   