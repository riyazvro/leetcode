class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        firstHCnt=0
        secHCnt=0
        vowels={'a','e','i','o','u'}
        half=len(s)/2
        for i in range(half):
            if s[i].lower() in vowels:
                firstHCnt+=1
            if s[i+half].lower() in vowels:
                secHCnt+=1
        return secHCnt==firstHCnt

            
        