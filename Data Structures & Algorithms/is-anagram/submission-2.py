class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = {}
        hash_t = {}
        if len(s) != len(t):
            return False
        for alph in s:
            hash_s[alph] = hash_s.get(alph,0)+1
        for alph in t:
            hash_t[alph] = hash_t.get(alph,0)+1
        return hash_s == hash_t