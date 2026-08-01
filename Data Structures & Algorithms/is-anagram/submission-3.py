class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        if len(s) != len(t):
            return False
        for alph in s:
            hashmap[alph] = hashmap.get(alph,0)+1
        for alph in t:
            if alph not in hashmap:
                return False
            hashmap[alph] -= 1
            if hashmap[alph] < 0:
                return False
        return True