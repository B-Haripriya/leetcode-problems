class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        l=set()
        for i in range(len(words)):
            for j in words[i]:
                if j==x:
                    l.add(i)
        return list(l)            