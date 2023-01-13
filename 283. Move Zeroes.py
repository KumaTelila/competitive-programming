class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero  =  nums.count(0)
        for i in range(zero):
            nums.remove(0)
            nums.append(0)
        # for i in nums:
        #     if(i==0):
        #         nums.remove(i)
        #         print("removed")
        # for i in range(zero):
        #     nums.append(0)
        # print(nums)
        # new_zero = nums.count(0)
        # for i in range(new_zero-zero):
        #     nums.pop()
        # print(new_zero)
        print(zero)
        """
        Do not return anything, modify nums in-place instead.
        """