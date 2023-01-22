class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        ls = sorted(nums)
        i = 0
        j = len(ls)-1
        lst  = []
        while(i<j):
            sum = ls[i]+ls[j]
            lst.append(sum)
            i+=1
            j-=1
        lst.sort()
        print(lst)
        return lst[-1]