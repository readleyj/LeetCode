class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_differences = Counter(ransomNote) - Counter(magazine)
        return not any(count_differences.values())
