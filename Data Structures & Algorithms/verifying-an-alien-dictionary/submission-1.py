class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        pos = {}
        for index, letter in enumerate(order):
            pos[letter] = index
        
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]

            for c in range(len(w1)):
                if c >= len(w2):
                    return False
                if w1[c] != w2[c]:
                    if pos[w1[c]] > pos[w2[c]]:
                        return False
                    break
        return True