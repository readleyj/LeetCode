class Solution:
    def reverseString(self, s: List[str]) -> None:
        left_ptr, right_ptr = 0, len(s) - 1

        while left_ptr < right_ptr:
            left_char, right_char = s[left_ptr], s[right_ptr]
            s[left_ptr], s[right_ptr] = right_char, left_char
            left_ptr, right_ptr = left_ptr + 1, right_ptr - 1
