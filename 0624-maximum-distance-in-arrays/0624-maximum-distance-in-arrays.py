class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        MAX = 10**4 + 1
        min_1, min_2 = (MAX, -1), (MAX, -1)
        max_1, max_2 = (-MAX, -1), (-MAX, -1)

        for i, arr in enumerate(arrays):
            now_min, now_max = arr[0], arr[-1]

            if now_min < min_1[0]:
                min_2 = min_1
                min_1 = (now_min, i)
            elif now_min < min_2[0]:
                min_2 = (now_min, i)
            
            if now_max > max_1[0]:
                max_2 = max_1
                max_1 = (now_max, i)
            elif now_max > max_2[0]:
                max_2 = (now_max, i)

        if min_1[1] != max_1[1]:
            return abs(max_1[0]-min_1[0])

        return max(abs(max_1[0]-min_2[0]), abs(max_2[0]-min_1[0]))
