class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_dict = {}
        for item in strs:
            signature = ''.join(sorted(item)) 
            if signature not in sorted_dict.keys():
                sorted_dict[signature] = []
            sorted_dict[signature].append(item)
        return list(sorted_dict.values())