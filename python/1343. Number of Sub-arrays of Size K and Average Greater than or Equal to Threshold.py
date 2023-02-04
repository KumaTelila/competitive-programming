class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        c = 0
        sum1 = sum(arr[0: k])
        av = sum1/k
        for i in range(1, len(arr)-k+1):
            av = sum1/k
            if av >=threshold:
                c+=1
            sum1 = (sum1 -arr[i-1] )+arr[i+k-1]
        if av>=threshold:
            c+=1
        return c
