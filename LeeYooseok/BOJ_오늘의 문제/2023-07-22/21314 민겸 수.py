mk_num = input()
len_mk = len(mk_num)

# 최댓값 : K는 최대한 앞에 많은 M을 붙인다. M은 단독으로 사용
# 최솟값 : M끼리 붙이고, K는 단독
m_cnt = 0
max_num = ''
min_num = ''
for idx in range(len_mk):
    if mk_num[idx] == 'M':
        m_cnt += 1
    else:
        max_num += '5' + '0' * m_cnt

        if m_cnt > 0:
            min_num += '1' + '0' * (m_cnt - 1)
        min_num += '5'

        m_cnt = 0

if m_cnt > 0:
    max_num += '1' * m_cnt
    min_num += '1' + '0' * (m_cnt - 1)
print(max_num)
print(min_num)