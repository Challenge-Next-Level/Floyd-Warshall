# 연간 납부 금액 : 최근 12개월간의 납부금액의 총 합

def check_VIP(n_month, payments):
    if 24 <= n_month < 60:
        year_pay = sum(payments)
        if year_pay >= 900000:
            return True
    elif 60 <= n_month:
        year_pay = sum(payments)
        if year_pay >= 600000:
            return True
    return False


def solution(periods, payments, estimates):
    # 이번달에 VIP 아니지만 다음달에 VIP 인 고객의 수, 이번달에 VIP 이지만 다음달에 VIP 가 아니게 되는 고객의 수
    answer = [0, 0]

    n_customers = len(periods)

    for i in range(n_customers):
        # 가입 개월 수
        n_month = periods[i]

        # 납부 내역
        cus_payment = payments[i]

        # 다음달 납부 예정
        cus_estimate = estimates[i]

        # 이번달에 VIP 인지 확인 - 가입 개월 수, 최근 12개월 간의 납부 이력
        old_VIP = check_VIP(n_month, cus_payment[-12:])

        # 다음달에 VIP 인지 확인 - 가입 개월 수, 최근 12개월 간의 납부 이력
        n_month += 1
        cus_payment.append(cus_estimate)
        new_VIP = check_VIP(n_month, cus_payment[-12:])

        if not old_VIP and new_VIP:
            answer[0] += 1
        elif old_VIP and not new_VIP:
            answer[1] += 1
    return answer


solution([20, 23, 24], [[100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000], [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000], [350000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000]], [100000, 100000, 100000])