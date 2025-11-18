class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        track=set()
        while n not in track:
            s=str(n)
            revsum=0
            for c in s:
                revsum+=int(c)**2
            if revsum==1:
                return True
            else:
                track.add(n)
            n=revsum
        return False
            

        