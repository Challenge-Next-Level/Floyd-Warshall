SELECT mcdp_cd as '진료과코드', COUNT(*) as '5월예약건수'
FROM appointment
WHERE DATE_FORMAT(apnt_ymd, '%Y-%m') = '2022-05'
# WHERE apnt_ymd LIKE '2022-05%'
GROUP BY mcdp_cd
ORDER BY COUNT(*) , mcdp_cd