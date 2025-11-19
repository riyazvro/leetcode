class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        count={}
        for c in arr:
            count[c]=1+count.get(c,0)
        for c in arr:
            if count[c]==1:
                k-=1
                if k==0:
                    return c
        return ""
    
        