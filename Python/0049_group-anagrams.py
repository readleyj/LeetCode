class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = dict()

        for word in strs:
            sorted_word = ''.join(sorted(word))

            if sorted_word not in anagram_map:
                anagram_map[sorted_word] = []

            anagram_map[sorted_word].append(word)

        return anagram_map.values()
