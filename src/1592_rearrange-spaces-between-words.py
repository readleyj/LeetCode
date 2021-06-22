class Solution:
    def reorderSpaces(self, text: str) -> str:
        num_spaces = text.count(' ')
        words = text.split(' ')
        words = [word for word in words if word]

        if len(words) == 1:
            return words[0] + ' ' * num_spaces

        delimeter = ' ' * (num_spaces // (len(words) - 1))
        extra_spaces = ' ' * (num_spaces % (len(words) - 1))

        return delimeter.join(words) + extra_spaces
