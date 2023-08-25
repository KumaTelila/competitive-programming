class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        ls = []
        for i in nums:
            ls.append(int(i))
        ls.sort()
        ls.reverse()
        a = ls[k-1]
        print(a)
        print (ls)
        return str(a)