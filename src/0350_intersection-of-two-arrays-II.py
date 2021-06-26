class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        occurence_counts = Counter(nums1) & Counter(nums2)
        return occurence_counts.elements()
