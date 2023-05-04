class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char == "(":
                stack.append(char)
            elif char == ")":
                if not stack or stack[-1] != "(":
                    return False
                else:
                    stack.pop()
            elif char == "{":
                stack.append(char)
            elif char == "}":
                if not stack or stack[-1] != "{":
                    return False
                else:
                    stack.pop()
            elif char == "[":
                stack.append(char)
            elif char == "]":
                if not stack or stack[-1] != "[":
                    return False
                else:
                    stack.pop()


        if len(stack) == 0:
            return True
        return False
