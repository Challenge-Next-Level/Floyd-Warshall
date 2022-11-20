SELECT dr_name, dr_id, mcdp_cd, DATE_FORMAT(hire_ymd, '%Y-%m-%d') as hire_ymd
FROM DOCTOR
WHERE (mcdp_cd = 'CS' or mcdp_cd = 'GS')
ORDER BY hire_ymd DESC, dr_name