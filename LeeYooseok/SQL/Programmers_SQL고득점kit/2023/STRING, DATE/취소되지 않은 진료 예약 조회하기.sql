SELECT a.apnt_no, p.pt_name, p.pt_no, a.mcdp_cd, d.dr_name, a.apnt_ymd
FROM
    (SELECT apnt_ymd, apnt_no, pt_no, mcdp_cd, mddr_id
     FROM appointment
     WHERE apnt_ymd LIKE '2022-04-13%' AND apnt_cncl_yn = 'N') as a, patient as p, doctor as d
WHERE a.pt_no = p.pt_no AND d.dr_id = a.mddr_id
ORDER BY apnt_ymd