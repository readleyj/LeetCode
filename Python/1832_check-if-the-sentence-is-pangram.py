class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet = string.ascii_lowercase
        letter_set = set()

        for char in sentence:
            letter_set.add(char)

        for letter in alphabet:
            if letter not in letter_set:
                return False

        return True
