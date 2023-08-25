class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        l,r = 0, len(arr)-1
        m = arr[r//2]
        sol = []
        while(l<=r):
            if abs(arr[l]-m) > abs(arr[r]-m):
                sol.append(arr[l])
                l+=1
            else:
                sol.append(arr[r])
                r-=1
        return sol[:k]
