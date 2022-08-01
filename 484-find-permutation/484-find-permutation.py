class Solution:
    def findPermutation(self, s: str) -> List[int]:
        result = []
        small = 1
        d_count = 0
        
        for char in s :
            if char == "I":
                for d in range(d_count):
                    result.append(small+d_count-d)
                result.append(small)
                small += 1 + d_count
                d_count = 0
            elif char == "D":
                d_count += 1
        
        if s[-1] == "D":
            for d in range(d_count):
                result.append(small+d_count-d)
        
        if s[-1] == "I":
            result.append(len(s) + 1)
        elif s[-1] == "D":
            result.append(result[-1] - 1)
        
        return result
        

"""
I -> [1,2]
D -> [2,1]
II -> [1,2,3]
DD -> [3,2,1]
ID -> [1,3,2]
DI -> [2,1,3]

III -> [1,2,3,4]
IID -> [1,2,4,3]
IDI -> [1,3,2,4] 
DII -> [2,1,3,4]
 
IDD -> [1,4,3,2] 
DID -> [2,1,4,3] ## [2,1,4,2]
DDI -> [3,2,1,4]
DDD -> [4,3,2,1]


1. 맨 왼쪽에 있는 D는 최대값이 된다.
2. 맨 왼쪽에 있는 I는 최소값(1)이 된다.
2. D가 마지막이라면, 마지막값 = 앞에있었던 I의 개수 + 1
3. I가 마지막이라면, 마지막값 = 앞에있었던 (최대숫자 - 앞에있었던 D의 개수)

"I"
"DI"
"III"
"IID"
"IDI"
"DII"
"IDD"
"DID"
"DDI"
"DDD"
"""