class Solution:
    def countSegments(self, s: str) -> int:
        count=0
        for i in (s.strip(' ').split(' ')):
            if i != '':
                count += 1
        return count