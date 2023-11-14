class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        """
        two pointer approach by iterating upto sqrt of c
        """
        j = int(sqrt(c))
        i =0
        while i<=j:
            if (i*i) + (j*j) == c:
                return True
            elif (i*i) + (j*j) >c:
                j-=1
            else:
                i+=1
        return False
