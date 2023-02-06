class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = {}
        sum = 0
        c = 0
        mp[0] = 1
        print(mp)
        for i in nums:
            sum +=i
            if sum-k in mp:
                c+=mp[sum-k]
            if sum not in mp:
                mp[sum] = 1
            else:
                mp[sum] = mp[sum]+1
        return c
