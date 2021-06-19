class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        running_max = -1

        for idx in reversed(range(len(arr))):
            num = arr[idx]
            arr[idx] = running_max
            running_max = max(num, running_max)

        return arr
