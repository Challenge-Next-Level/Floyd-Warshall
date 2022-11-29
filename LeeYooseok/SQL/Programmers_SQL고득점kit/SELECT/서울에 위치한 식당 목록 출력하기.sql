# 식당 ID, 식당 이름, 음식 종류, 즐겨찾기수, 주소, 리뷰 평균 점수
SELECT i.rest_id, i.rest_name, i.food_type, i.favorites, i.address, ROUND(AVG(r.review_score), 2) as avg_score
FROM rest_review r JOIN rest_info i ON r.rest_id = i.rest_id
WHERE i.address LIKE '서울%'
GROUP BY r.rest_id
ORDER BY avg_score DESC, i.favorites DESC