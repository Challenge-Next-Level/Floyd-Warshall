-- median 값을 추출하는 것, 오라클은 이런 함수도 제공하네
SELECT ROUND(MEDIAN(lat_n),4)
FROM STATION;