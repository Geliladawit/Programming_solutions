# Problem: Frequency Tracker - https://leetcode.com/problems/frequency-tracker/description/

from collections import defaultdict

class FrequencyTracker:

    def __init__(self):
        self.count = defaultdict(int)
        self.freq_count = defaultdict(int)

    def add(self, number: int) -> None:
        old = self.count[number]
        new = old + 1

        if old > 0:
            self.freq_count[old] -= 1

        self.count[number] = new
        self.freq_count[new] += 1

    def deleteOne(self, number: int) -> None:
        if self.count[number] == 0:
            return
        
        old = self.count[number]
        new = old - 1

        self.freq_count[old] -= 1
        if new > 0:
            self.freq_count[new] += 1
        
        self.count[number] = new

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq_count[frequency] > 0


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)