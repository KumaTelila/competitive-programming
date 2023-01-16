class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ls = [0]*len(nums1)
        print(ls)
        for i in range(0, len(nums1)):
            found = 0
            foundI = 0
            for j in range(0, len(nums2)):
                if(nums1[i]==nums2[j]):
                    foundI = 1
                if(foundI == 1 and nums1[i]<nums2[j]):
                    ls[i] = nums2[j]
                    found = 1
                    break
            if(found==0):
                ls[i] = -1
        return ls
                