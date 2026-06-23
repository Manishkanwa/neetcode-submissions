class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq = {}
        t_freq = {}

        for i in s:
            if i in s_freq.keys():
                s_freq[i] += 1
            else :
                s_freq[i] = 1
        
        for i in t:
            if i in t_freq.keys():
                t_freq[i] += 1
            else :
                t_freq[i] = 1
        if s_freq == t_freq:
            return True
        else:
            return False