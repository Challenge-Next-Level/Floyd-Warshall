SELECT m.member_name, r.review_text, DATE_FORMAT(r.review_date, '%Y-%m-%d') as review_date
FROM member_profile as m, rest_review as r
WHERE m.member_id = r.member_id and m.member_id =
                                    (SELECT member_id
                                     FROM rest_review
                                     GROUP BY member_id
                                     ORDER BY COUNT(*) DESC LIMIT 1)
ORDER BY r.review_date, r.review_text