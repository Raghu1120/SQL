class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        mer = nums1[:m] + nums2[:n]
        mer.sort()
        nums1[:] = mer