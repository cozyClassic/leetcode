import heapq
class MyCalendar:
    def __init__(self):
        self.schedules = []

    def book(self, start: int, end: int) -> bool:
        for s_s, s_e in self.schedules :
            if end <= s_s or s_e <= start :
                continue
            else:
                return False
        self.schedules.append((start,end))            
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)

"""
s_s,   s_e

S, E 

E <= s_s or s_e <= S :
continue

"""