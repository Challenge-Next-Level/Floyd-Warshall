SELECT C.CAR_ID
FROM CAR_RENTAL_COMPANY_CAR AS C
WHERE C.CAR_ID IN (SELECT CAR_ID FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY WHERE START_DATE LIKE '%-10-%') AND C.CAR_TYPE = '세단'
ORDER BY CAR_ID DESC