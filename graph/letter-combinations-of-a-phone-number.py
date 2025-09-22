class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        result = []

        digit_map = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }
        
        if not digits:
            return result

        def backtrack(index, elem):
            if index == len(digits):
                result.append("".join(elem))
                return

            cur_num = digits[index]
            letters = digit_map[cur_num]

            for letter in letters:
                elem.append(letter)
                backtrack(index+1, elem)
                elem.pop()

        backtrack(0, [])
        
        return result
