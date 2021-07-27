class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        comp_list = nums1 + nums2
        comp_list.sort()
        comp_length = len(comp_list)
        remainder = comp_length % 2

        if remainder == 1:
            median_index = int((comp_length - 1) / 2)
            median = comp_list[median_index]
        elif remainder == 0:
            index_one = int(comp_length / 2)
            index_two = int(index_one - 1)
            median = (comp_list[index_two] + comp_list[index_one]) / 2
        return median
