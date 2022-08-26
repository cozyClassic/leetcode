from collections import Counter
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        twos = [Counter("1")]
        x = 1
        while x < 10**9 :
            x*= 2
            twos.append(Counter(str(x)))
        
        return Counter(str(n)) in twos
        

"""
n을 주고 재배치를 해라. (0이 안되도록)
만약 얘네들을 재배치했을 때, 2의 배수가 될 수 있다면

"""