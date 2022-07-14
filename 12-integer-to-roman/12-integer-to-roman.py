class Solution:
    def intToRoman(self, num: int) -> str:
        result = ""
        d = {"IV":4,"IX":9, "XL":40,"XC":90,"CD":400,"CM":900,
             "M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
        
        thousand = num//1000
        t = {3:"MMM",2:"MM",1:"M" ,0:""}
        result += t[thousand]
        
        hundred = (num%1000)//100
        h = {9:"CM",8:"DCCC",7:"DCC",6:"DC",5:"D",4:"CD",3:"CCC",2:"CC",1:"C",0:""}
        result += h[hundred]
        
        ten = (num%100)//10
        t2 = {9:"XC",8:"LXXX",7:"LXX",6:"LX",5:"L",4:"XL",3:"XXX",2:"XX",1:"X",0:""}
        result += t2[ten]
        
        one = (num%10)
        o = {9:"IX",8:"VIII",7:"VII",6:"VI",5:"V",4:"IV",3:"III",2:"II",1:"I",0:""}
        result += o[one]
        
        return result