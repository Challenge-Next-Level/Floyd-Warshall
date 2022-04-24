s = input()

needs = 0 # 추가로 필요한 문자열 길이
for i in range(len(s)):
    if s[i] != s[-1]: # 맨 뒤 문자와 같은 것을 찾는다
        continue
    total_length = len(s[i:]) # 이 길이 만큼 팰린드롬이라 우선 가정
    length = total_length // 2 # 절반을 비교하여 팰린드롬인지 판별
    if s[i:i + length] == s[:-length-1:-1]: # 맞다면
        needs = i # 앞에 팰린드롬이 아닌 부분 만큼 길이 필요
        break
print(len(s) + needs)