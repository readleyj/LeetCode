class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        num_consecutive = 0

        for num in arr + [0]:
            if num % 2:
                num_consecutive += 1

                if num_consecutive == 3:
                    return True
            else:
                num_consecutive = 0

        return False
