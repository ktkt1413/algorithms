def checkPalindrome( s, l, r, palindrome_sub, palindrome_len):
    while l >= 0 and r <len(s) and s[l] == s[r]:  # 이 부분이 만족하지 않으면 while문이 끝남
        if palindrome_len < ( r - l + 1 ):  # 'r - l + 1' 은 현재 펠린드롬으로 설정되어 있는 값( 현재 펠린드롬과 다를수있음)
            palindrome_sub = s[ l : r + 1 ]  # 설정 값과 현재 펠린드롬 문자가 다르다면 설정값을 없데이트 시켜줘야함
            palindrome_len = r - l + 1  # 마찬가지로 펠린드롬 길이 값을 없데이트해야함
        l -= 1
        r += 1   # 오른쪽, 왼쪽으로 한칸씩 이동하여 더 큰 펠린드롬이 있는지 확인한다

    return palindrome_len, palindrome_sub

class Palindrome:
    def logestPalindrome(self, s: str) -> str:  # s는 str, ->str 은 반환 값도 str
        palindrome_len = 0
        palindrome_sub = ' '

        for i in range(len(s)):
            palindrome_sub, palindrome_len = checkPalindrome( s , i, i, palindrome_sub, palindrome_len) # 펠린드롬이 홀수 일때, i=i 인 이유

            palindrome_sub, palindrome_len = checkPalindrome(s, i, i+1 , palindrome_sub, palindrome_len) # 펠린드롬이 짝수 일때, i, i+1 인 이유

        return palindrome_sub


# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#
#
#     result = ""  # 가장 긴 부분 팰린드롬을 저장하는 변수
#
#     for i in range(len(s)):  # 문자열의 길이만큼 반복
#         if len(s) - i <= len(result):  # 큰 문자열 -> 작은 문자열로 진행되기에 결과값 문자열보다 작아진다면 종료
#         break
#     for j in range(len(s), i, -1):  # 큰 문자열 -> 작은 문자열 순서로 반복
#         if len(s[i:j]) <= len(result):  # 마찬가지로 결과값보다 길이가 작으면 종료
#         break
#     if s[i:j] == s[i:j][::-1]:  # 문자열을 뒤집어도 같은지 확인
#         result = s[i:j]  # 같다면 결과값에 추가 (결과값보다 길이가 큰 조건)
#     break
#     return result
