SELECT member_id,member_name,gender,TO_CHAR(date_of_birth,'yyyy-mm-dd') FROM MEMBER_PROFILE
WHERE tlno is not null AND EXTRACT(MONTH from date_of_birth) = 3 AND gender = 'W'
ORDER BY member_id;