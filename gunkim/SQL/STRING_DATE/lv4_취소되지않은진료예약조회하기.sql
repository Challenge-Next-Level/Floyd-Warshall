SELECT A.apnt_no, P.pt_name, P.pt_no, D.mcdp_cd, D.dr_name, A.apnt_ymd
FROM PATIENT P, DOCTOR D, APPOINTMENT A
WHERE P.pt_no = A.pt_no AND D.dr_id = A.mddr_id AND A.apnt_cncl_yn = 'N'
AND A.apnt_ymd LIKE '2022-04-13%'
ORDER BY A.apnt_ymd