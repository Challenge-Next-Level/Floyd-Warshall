import heapq


def solution(jobs):
    job_count = len(jobs)
    time = 0
    total_wait_time = 0

    heapq.heapify(jobs)
    request_jobs = list()

    while jobs or request_jobs:
        while jobs and jobs[0][0] <= time:
            job = heapq.heappop(jobs)
            heapq.heappush(request_jobs, [job[1], job[0]])  # 소요 시간, 요청 시각

        if request_jobs:
            request_job = heapq.heappop(request_jobs)
            time += request_job[0]
            total_wait_time += (time - request_job[1])
        else:
            time += 1

    return total_wait_time // job_count