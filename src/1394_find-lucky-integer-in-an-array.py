class Solution:
    def findLucky(self, arr: List[int]) -> int:
        lucky_int = -1
        counts = Counter(arr)

        for num, count in counts.items():
            if num == count:
                lucky_int = max(num, lucky_int)

        return lucky_int
