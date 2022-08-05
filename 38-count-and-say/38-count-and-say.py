class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        say_list = []
        say = self.countAndSay(n-1)
        for num in say :
            num = int(num)
            if not say_list or say_list[-1][1] != num :
                say_list.append([1,num])
            else :
                say_list[-1][0] += 1
        
        result = ""
        for num, count in say_list:
            result += str(num) + str(count)
                
        return result