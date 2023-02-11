class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        mp = defaultdict(int)
        mp[0] = 1
        c, result = 0, 0
        for i in range(len(nums)):
            if nums[i]%2!=0: c+=1
            result += mp[c-k]
            mp[c]+=1
        return result