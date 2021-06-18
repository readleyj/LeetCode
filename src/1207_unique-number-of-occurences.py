class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        num_occurences = Counter(arr)
        occurences_set = set()

        for num in set(arr):
            count = num_occurences[num]

            if count in occurences_set:
                return False
            else:
                occurences_set.add(count)

        return True
