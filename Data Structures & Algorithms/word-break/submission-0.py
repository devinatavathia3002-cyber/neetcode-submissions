class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if dp[i]:
                    break
                if len(word) > len(s[i:]):
                    continue
                if word == s[i: len(word) + i]:
                    print("here")
                    dp[i] = dp[i + len(word)]


        return dp[0]