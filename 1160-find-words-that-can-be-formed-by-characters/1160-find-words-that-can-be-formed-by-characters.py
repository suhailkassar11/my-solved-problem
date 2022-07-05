class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = 0
        for x in words:
            word = list(chars)
            for y in x:
                if y not in word:
                    break
                else:
                    word.remove(y)
            else:
                count += len(x)

        return count