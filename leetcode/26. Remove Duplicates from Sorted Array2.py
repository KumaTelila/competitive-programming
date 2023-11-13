class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r =0, 1
        while r<len(nums) and nums[r] != 101:
            if nums[l] == nums[r]:
                del nums[r]
                nums.append(101)
            else:
                l+=1
                r+=1
            
        return len(nums) - nums.count(101)