def is_valid_parenthesis(self, s: str) -> bool:
    pair = {
        '}': '{',
        ')': '(',
        ']': '[',
    }
    opener = "({["
    stack = []

    for char in s:
        if char in opener:
            stack.append(char)

        elif not stack or pair[char] != stack.pop():
            return False

        return len(stack) == 0


        # else:
        #     if not stack:
        #         return False
        #     top = stack.pop()  # stack.pop() -> 자체가 이미 스택에서 가장 윗 부분의 노드를 꺼냄 -> top에 할당
        #     if pair[char] != top:
        #         return False

    return not stack  # stack이 비어있으면 true, 그렇지 않으면 false 를 반환한다

#test코드
assert is_valid_parenthesis("()")
assert is_valid_parenthesis("()[]{}")  #유효한 문자라면 true를 반환하는지 확인하고, Assertionerror가 발생하지 않아야 함
assert not is_valid_parenthesis("(]")  #유효하지 않는 문자라면 false를 반환하는지 확인하고, Assertionerror가 발생하지 않아야 함




# Given a string s containing just the characte'(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.
# 3. Every close bracket has a corresponding open bracket of the same type.

#Example 1:
# Input: s = "()"
# Output: true
# Example 2:
# Input: s = "()[]{}"
# Output: true
# Example 3:
# Input: s = "(]"
# Output: false
# Constraints:
# * 1 <= s.length <= 104
# * s consists of parentheses only '()[]{}'.


