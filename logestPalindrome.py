def checkPalindrome( s, l, r, palindrome_sub, palindrome_len):
    while l >= 0 and r <len(s) and s[l] == s[r]:
        if palindrome_len < ( r - l + 1 ):  # 'r - l + 1' 은 현재 펠린드롬으로 설정되어 있는 값( 현재 펠린드롬과 다를수있음)
            palindrome_sub = s[ l : r + 1 ]  # 설정 값과 현재 펠린드롬 문자가 다르다면 설정값을 없데이트 시켜줘야함
            palindrome_len = r - l + 1  # 마찬가지로 펠린드롬 길이 값을 없데이트해야함
        l -= 1
        r += 1   # 오른쪽, 왼쪽으로 한칸씩 이동하여 더 큰 펠린드롬이 있는지 확인한다

    return palindrome_len, palindrome_sub

class Solution:
    def logestPalindrome(self, s: str) -> str:  # s는 str, ->str 은 반환 값도 str
        palindrome_len = 0
        palindrome_sub = ' '

        for i in range(len(s)):
            palindrome_sub, palindrome_len = checkPalindrome( s , i, i, palindrome_sub, palindrome_len) # 펠린드롬이 홀수 일때, i=i 인 이유

            palindrome_sub, palindrome_len = checkPalindrome(s, i, i+1 , palindrome_sub, palindrome_len) # 펠린드롬이 짝수 일때, i, i+1 인 이유

        return palindrome_sub


