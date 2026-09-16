class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not len(s) == len(t):
            return False
        s_sorted = sorted(s)
        t_sorted = sorted(t)
        for i,_ in enumerate(s_sorted):
            if not s_sorted[i] == t_sorted[i]:
                return False

        return True