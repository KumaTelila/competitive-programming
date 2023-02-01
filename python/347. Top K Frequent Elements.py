class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        for i in nums:
            if(i in mp):
                mp[i]+=1
            else:
                mp[i] = 1
        
        mp = sorted(mp.items(), key=lambda x:x[1], reverse=True)
        converted_dict = dict(mp)
        ls = list(converted_dict.keys())
        print(converted_dict)
        print(ls[:k])
        return ls[:k]