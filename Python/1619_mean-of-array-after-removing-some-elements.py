class Solution:
    def trimMean(self, arr: List[int]) -> float:
        threshold = round(len(arr) / 20)
        modified_arr = sorted(arr)[threshold:len(arr) - threshold]
        return sum(modified_arr) / len(modified_arr)
