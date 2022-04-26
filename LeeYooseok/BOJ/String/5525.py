n = int(input())

result = 0

# pn = "IO" * n + "I"
# length_pf = 2*n+1

m = int(input())

s = input()

# for i in range(m - length_pf + 1):
#     if s[i] == s[i+1] or s[i] == "O":
#         pass
#     if s[i:i+length_pf] == pn:
#         result += 1

pattern = 0
i = 1
while i < m-1:
    temp = s[i-1:i+2]
    if temp == "IOI":
        pattern += 1
        if pattern == n:
            pattern -= 1
            result += 1
        i += 1
    else:
        pattern = 0

    i += 1

print(result)