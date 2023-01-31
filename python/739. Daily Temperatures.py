class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ls = [0]*len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while(len(stack)>0 and temperatures[stack[-1]]<temperatures[i]):
                j = stack.pop()
                ls[j] = i-j
            stack.append(i)
        return ls