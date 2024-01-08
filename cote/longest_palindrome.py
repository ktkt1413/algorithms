#  sol. 가장 긴 펠린드롬을 확인할 때, 문자열의 바깥에서 안쪽으로 확인하면 시간을 줄일 수 있다.
#  방법1. 짧은 팰린드롬 -> 긴 펠린드롬

def checkPalindrome(s, l, r, palindrome_len, palindrome_sub):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        length = r - l + 1    #  = 현재 펠린드롬 길이
        if palindrome_len < length:
            palindrome_sub = s[ l : r + 1]
            palindrome_len = length
        l -= 1
        r += 1

    return palindrome_len, palindrome_sub

class Palindrome:
    def longestPalindrome(self, s: str) -> str:
        palindrome_len = 0
        palindrome_sub = ""

        for i in range(len(s)):
            palindrome_len, palindrome_sub = checkPalindrome(s, i, i, palindrome_len, palindrome_sub)
            palindrome_len, palindrome_sub = checkPalindrome(s, i, i+1, palindrome_len, palindrome_sub)

        return palindrome_sub

example_string = "babad"
palindrome_instance = Palindrome()
result = palindrome_instance.longestPalindrome(example_string)
print("Longest Palindrome Substring:", result)

#  sol.2  긴 펠린드롬 -> 짧은 펠린드롬

class Solution2:
    def longestPalindrome2(self, s:str) -> str:
        result = ""

        for i in range(len(s)):
            if len(s) - i + 1 <= len(result):
                break
            for j in range(len(s), i, -1):  #  range(len(s), i, -1) = reverse
                if len(s[i:j]) < len(result):   #  ex) range(5,0,-1) = 5, 4, 3, 2, 1
                    break
                if s[i:j] == s[i:j][::-1]:   # [::-1] = reverse
                    result = s[i:j]
                    break
        return result

substring = "abbdaggtttsstttggadbbasr"
palind = Solution2()
resul = palind.longestPalindrome2(substring)

print("longest:", resul)