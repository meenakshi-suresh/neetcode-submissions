class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {
            'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000
        }
        res = 0
        max_val = 0
        
        # Iterate from right to left safely
        for i in range(len(s) - 1, -1, -1):
            curr_val = romans[s[i]]
            
            # If current value is less than the max seen to its right, subtract it
            if curr_val < max_val:
                res -= curr_val
            else:
                res += curr_val
                max_val = curr_val # Update the highest value seen so far
                
        return res
