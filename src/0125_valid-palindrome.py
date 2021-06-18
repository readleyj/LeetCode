class Solution:
    def isPalindrome(self, s: str) -> bool:
        concat_chars = [char for char in s.lower() if char.isalnum()]
        return concat_chars == concat_chars[::-1]
