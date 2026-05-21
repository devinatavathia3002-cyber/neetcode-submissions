class Solution:
    def checkValidString(self, s: str) -> bool:
        
        star = []
        openS = []

        for i in range(len(s)):
            char = s[i]
            if char == ")":
                if len(openS) > 0:
                    openS.pop()
                elif len(star) > 0:
                    star.pop()
                else:
                    return False
            elif char == "(":
                openS.append(i)
            else:
                star.append(i)
        
        if len(openS) > len(star):
            return False
        while openS:
            openIndex = openS.pop()
            starIndex = star.pop()
            if starIndex <= openIndex:
                return False

        return True