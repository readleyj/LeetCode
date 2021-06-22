class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        arr_set = set(arr)
        cur_missing, num_missing = 1, 0

        while num_missing != k:
            if cur_missing not in arr_set:
                num_missing += 1

            cur_missing += 1

        return cur_missing - 1
