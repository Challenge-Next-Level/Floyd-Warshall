-- 리뷰는 여러개이기 때문에 REST_INFO 테이블이 중복되어 많이 조회됨, 따라서 GROUP BY로 해결해야 함.
-- 주소가 서울인 곳을 처음엔 SUBSTR로 처리했는데 LIKE로 변경하여 정답처리됨.
SELECT ri.rest_id,ri.rest_name,ri.food_type,ri.favorites,ri.address,ROUND(AVG(rr.review_score),2) as average
FROM REST_INFO ri, REST_REVIEW rr
WHERE ri.rest_id = rr.rest_id AND ri.address LIKE '서울%'
GROUP BY ri.rest_id,ri.rest_name,ri.food_type,ri.favorites,ri.address
ORDER BY average DESC, ri.favorites DESC;