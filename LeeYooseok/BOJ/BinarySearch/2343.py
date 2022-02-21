n, m = map(int, input().split())
videos = list(map(int, input().split()))

total = sum(videos)

start, end = max(videos), total # 시작을 max(videos) 로 해줘야지 풀린다? -> 최소 한 블루레이 크기에 한 음악(최대 크기)은 들어갈 수 있도록 해줘야 한다.
result = 0


def check(size):
    # 앞에서부터 가능하게 해서 개수 센다.
    cnt = 0
    nowSize = 0
    for v in videos:
        if nowSize + v > size:
            cnt += 1
            nowSize = 0

        nowSize += v

    if nowSize > 0:
        cnt += 1

    if cnt > m:
        return False
    else:
        return True


while start <= end:
    mid = (start + end) // 2

    # 해당 길이가 가능한 블루레이 크기 일 때
    if check(mid):
        result = mid
        end = mid - 1
    else:
        start = mid + 1

print(result)