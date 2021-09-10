class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed)
        count_consistent = 0

        for word in words:
            count_consistent += 1

            for char in word:
                if char not in allowed_set:
                    count_consistent -= 1
                    break

        return count_consistent
