class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """   
        intervals = sorted(intervals)
        
        for i in range(len(intervals) - 1):
            if(intervals[i][1] > intervals[i + 1][0]):
                return False
            
        return True

print(Solution().canAttendMeetings([[0,30],[5,10],[15,20]]))