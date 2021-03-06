class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        while start < end:
            mid = (start + end) // 2
            if (isBadVersion(mid)):
                end = mid
            else:
                start = mid + 1
        return start
        
