class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        output = []
        for i in range(len(r)):
            j = nums[l[i]:r[i]+1]
            j.sort(reverse = True)
            # print(j)
            if len(j) >= 2:
                x = j[0]
                y = j[1]
                right = 2
                res = x - y
                while(right < len(j)):
                    y = j[right]
                    x = j[right - 1] 
                    if x - y != res:
                        output.append(False)
                        break
                    right += 1
                if len(output) < i + 1:
                    output.append(True)
            else:
                output.append(False)
            # print(output)
        return output