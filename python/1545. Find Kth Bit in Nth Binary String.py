class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = "0" 
        i = 1
        while(i<=n):
            inverted = s
            inverted = inverted.replace('1', '2')
            inverted = inverted.replace('0', '1')
            inverted = inverted.replace('2', '0')
            rvsd = inverted
            rvsd = "".join(reversed(rvsd))
            s = s + "1" + rvsd
            i+=1
        return s[k-1]