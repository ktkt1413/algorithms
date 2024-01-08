from lecture.linkedlist import LinkedList, Palindromes

l1 = LinkedList()
for num in [1, 2, 2, 1]:
    l1.append(num)
l2 = LinkedList()
for num in [1, 2]:
    l2.append(num)

assert Palindromes.palindrome(l1)
assert not Palindromes.palindrome(l2)

print(Palindromes.palindrome(l1))
print(Palindromes.palindrome(l2))






