class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()

        diff = [arr[idx] - arr[idx - 1] for idx in range(1, len(arr))]
        return all(diff[0] == diff[idx] for idx in range(len(diff)))
