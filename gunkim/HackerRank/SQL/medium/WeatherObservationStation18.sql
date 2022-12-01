-- 맨허튼 거리를 구하는 식인데 진짜 처음 들어보았다. 유클리드 거리보다 더 쉬운 거리 공식이라고 함.
SELECT ROUND(ABS(MIN(lat_n)-MAX(lat_n))+ABS(MIN(long_w)-MAX(long_w)),4)
FROM STATION;