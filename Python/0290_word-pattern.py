class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_map = dict()
        taken_chars = set()
        words = s.split(' ')

        if len(pattern) != len(words):
            return False

        for pattern_char, word in zip(pattern, words):
            if word not in pattern_map:
                pattern_map[word] = pattern_char

                if pattern_char in taken_chars:
                    return False

                taken_chars.add(pattern_char)
            elif pattern_map[word] != pattern_char:
                return False

        return True
