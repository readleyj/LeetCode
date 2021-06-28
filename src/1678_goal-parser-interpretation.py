class Solution:
    def interpret(self, command: str) -> str:
        left_par_open = False
        left_par_idx, right_par_idx = -1, -1

        result = ''

        for idx, char in enumerate(command):
            if char == 'G':
                result += char
            elif char == '(':
                left_par_open = True
                left_par_idx = idx
            elif char == ')':
                right_par_idx = idx

                if right_par_idx - left_par_idx > 1:
                    result += 'al'
                else:
                    result += 'o'

        return result
