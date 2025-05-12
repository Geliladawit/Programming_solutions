# Problem: My Calendar I - https://leetcode.com/problems/my-calendar-i/description/

class MyCalendar:

    def __init__(self):
        self.start = []
        self.end = []
        return

    def book(self, startTime: int, endTime: int) -> bool:
        for i in range(len(self.end)):
            if startTime < self.end[i] and endTime > self.start[i]:
                return False
        self.end.append(endTime)
        self.start.append(startTime)
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)