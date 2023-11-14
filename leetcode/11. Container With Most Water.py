class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        sum = 0

        while(l<r):
            area = min(height[l], height[r]) * (r-l)
            print(min(height[l], height[r]))
            if area > sum :
                sum = area
            if(height[l] == height[r]):
                l+=1
                r-=1
            elif height[l] < height[r]:
                l+=1
            elif height[l] > height[r]:
                r-=1
        return sum