def is_valid_parenthesis(s):
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
        else:
            if not stack:
                return False
            top = stack.pop()
            if pair[char] != top:
                return False

    return not stack

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


