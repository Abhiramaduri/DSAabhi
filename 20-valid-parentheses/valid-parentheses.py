class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
            
        stack = []
        for char in s:
            if char == '(':
                stack.append(')')
            elif char == '{':
                stack.append('}')
            elif char == '[':
                stack.append(']')
            # If stack is empty or the closing bracket doesn't match
            elif not stack or stack.pop() != char:
                return False
                
        return len(stack) == 0

