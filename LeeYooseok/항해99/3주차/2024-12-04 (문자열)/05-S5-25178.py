import sys

input = sys.stdin.readline

N = int(input())
A = input().rstrip()
B = input().rstrip()

if sorted(A) != sorted(B):
    print("NO")
    exit(0)

if A[0] != B[0] or A[-1] != B[-1]:
    print("NO")
    exit(0)

vowel_dict = {
    "a": "",
    "e": "",
    "i": "",
    "o": "",
    "u": ""
}

A_table = A.maketrans(vowel_dict)
A = A.translate(A_table)

B_table = B.maketrans(vowel_dict)
B = B.translate(B_table)

if A != B:
    print("NO")
    exit(0)

print("YES")
