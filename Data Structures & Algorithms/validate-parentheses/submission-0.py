class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        for bracket in s:
            if bracket in pairs.values():
                stack.append(bracket)
            else:
                if not stack:
                    return False
                if pairs[bracket] != stack[-1]:
                    return False
                stack.pop()
        if stack:
            return False
        return True
