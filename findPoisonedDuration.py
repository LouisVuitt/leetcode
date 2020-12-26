class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        ans = 0
        if len(timeSeries) !=0:
            for i in range(len(timeSeries)-1):
                if timeSeries[i+1] - timeSeries[i] >= duration:
                    ans = ans + duration
                else:
                    ans = ans + timeSeries[i+1] - timeSeries[i]
            return ans+duration
        else:
            return 0