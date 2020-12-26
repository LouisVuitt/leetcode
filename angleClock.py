class Solution(object):
    def angleClock(self, hour, minutes):
        angle = abs(5.5 * minutes - 30 * hour)
        if angle > 180:
            angle = 360 - angle
        return angle
