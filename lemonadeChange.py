class Solution(object):
    def lemonadeChange(self, bills):
        five = 0
        ten = 0
        twenty = 0
        for i in range(len(bills)):
            if bills[i] == 5:
                five = five + 1
            if bills[i] == 10:
                ten = ten + 1
                five = five -1
            if bills[i] == 20:
                twenty = twenty + 1
                if ten > 0:
                    ten = ten - 1
                    five = five - 1
                else:
                    five = five - 3
            if (five < 0) or (ten < 0):
                return False
        return True