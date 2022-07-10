class Solution(object):
    def findOriginalArray(self, changed):
        """
        :type changed: List[int]
        :rtype: List[int]
        """
        if (len(changed) % 2) !=0:
            return []
        
        res = []
        count = Counter(changed)
        for n in sorted(changed, key = abs):
            if count[n] == 0:
                continue
            if 2 * n not in count:
                return []
            count[n] -= 1
            count[2 * n] -= 1
            if count[2 * n] == 0:
                count.pop( 2 * n)
            res.append(n)
        return res

        