class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        for i in nums:
            if(i in mp):
                mp[i]+=1
            else:
                mp[i] = 1
        
        sorted_footballers_by_goals = sorted(mp.items(), key=lambda x:x[1], reverse=True)
        converted_dict = dict(sorted_footballers_by_goals)
        ls = list(converted_dict.keys())
        print(converted_dict)
        print(ls[:k])
        return ls[:k]