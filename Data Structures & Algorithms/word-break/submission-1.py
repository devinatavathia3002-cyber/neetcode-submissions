class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, - 1, -1):
            for word in wordDict:
                if dp[i]:
                    break
                if len(word) > len(s) - i:
                    continue
                if s[i: len(word) + i] == word and dp[len(word) + i]:
                    dp[i] = True

        return dp[0]