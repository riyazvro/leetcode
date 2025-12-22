class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        mints=6*minutes
        hrs=(30*hour)+(0.5*minutes)
        diff=abs(mints-hrs)
        return min(diff,360-diff)