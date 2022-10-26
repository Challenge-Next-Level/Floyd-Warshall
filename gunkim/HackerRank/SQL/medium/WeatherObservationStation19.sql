-- 이게 유클리드 거리(피타고라스 정리)
SELECT ROUND(SQRT(POWER(MAX(lat_n)-MIN(lat_n),2) + POWER(MAX(long_w)-MIN(long_w),2)),4)
FROM STATION;