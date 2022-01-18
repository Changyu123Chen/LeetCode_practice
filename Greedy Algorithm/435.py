class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort()
        sum = 0
        prev = intervals[0][1]
        for i in range (1,len(intervals)):
            prev = min(intervals[i][1], prev)
            if prev > intervals[i][0]:
                sum += 1
            else:
                prev = intervals[i][1]
        return(sum)
