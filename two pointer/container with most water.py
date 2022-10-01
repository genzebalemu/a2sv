class Solution(object):
    def maxArea(self, height):
        ans=0
        left = 0
        right=len(height)-1
        while left < right:
            area = (right- left) * min(height[left],height[right])
            ans= max (ans,area)
            if height[right] < height[left]:
                right -=1
            else:
                left +=1
        return ans