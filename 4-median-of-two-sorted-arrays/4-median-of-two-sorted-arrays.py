class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        nums1.extend(nums2)
        
        nums1.sort()
        
        if not len(nums1) % 2 == 0:
            return float(nums1[len(nums1)//2])
        
        n1 = nums1[len(nums1)//2]
        n2 = nums1[len(nums1)//2-1]
        
        return (n1+n2)/2