class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        num_triplets = 0

        for idx1 in range(len(arr)):
            for idx2 in range(idx1, len(arr)):
                for idx3 in range(idx2, len(arr)):
                    if idx1 != idx2 and idx2 != idx3 and idx1 != idx3:
                        num_triplets += (abs(arr[idx1] - arr[idx2]) <= a and abs(
                            arr[idx2] - arr[idx3]) <= b and abs(arr[idx1] - arr[idx3]) <= c)

        return num_triplets
