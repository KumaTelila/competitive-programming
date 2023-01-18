class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ls1 = sorted(intervals)
        ans = []
        ans.append(ls1[0])
        j = 0
        for i in range(1, len(ls1)):
            print(i)
            if ls1[i][0]<=ans[j][1]:
                print(i)
                print(ans[j][1])
                print((intervals[i][1]))
                print(max(ls1[i][1], ans[j][1]))
                ans[j][1] = max(ls1[i][1], ans[j][1])
                
            else:
                j+=1
                ans.append(ls1[i])
                

        print(ans)
        print(ls1)
        return ans