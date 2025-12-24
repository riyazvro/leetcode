class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        index=[]
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i]==needle[0]:
                for j in range(len(needle)):
                    if needle[j]!=haystack[i+j]:
                        break
                else:
                    index.append(i)
        return min(index) if index else -1

