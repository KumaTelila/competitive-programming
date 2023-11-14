class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        here is my two pointer approach
        by identifying the pattern of the array rotation
        1. rotate the entire arra
        2. rotate the array upto k elements
        3. rotate the rest array elements that means beyond the k
        """
        def rotate(arr, start, end):
            while start<end:
                arr[start], arr[end] = arr[end], arr[start]
                start+=1
                end-=1
        if k>len(nums):
            k%=len(nums)
        rotate(nums, 0, len(nums) -1)
        rotate(nums, 0, k-1)
        rotate(nums, k, len(nums) -1)
