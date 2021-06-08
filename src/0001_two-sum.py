class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {num: idx for idx, num in enumerate(nums)}

        for idx, num in enumerate(nums):
            if (lookup_num := target - num) in lookup:
                if (lookup_idx := lookup[lookup_num]) != idx:
                    return [idx, lookup_idx]

        return None
