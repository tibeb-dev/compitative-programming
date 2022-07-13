class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        monstk = []
        ans  = [0 for i in range(len(temperatures))]
        tem = temperatures
        for j, i in enumerate(tem):
            if not monstk:
                monstk.append([i, j])
            if i < monstk[-1][0]:
                monstk.append([i, j])
            else:
                while(monstk and monstk[-1][0]<i):
                    x = monstk.pop()
                    ans[x[1]] = j - x[1]
                monstk.append([i, j])
        return ans
            