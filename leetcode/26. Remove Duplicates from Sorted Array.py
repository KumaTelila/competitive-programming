class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        r = l
        while(r<=len(nums)-1):
            if(nums[l]<nums[r]):
                nums[l+1]= nums[r]
                l+=1
                r=l
            r+=1
        return l+1