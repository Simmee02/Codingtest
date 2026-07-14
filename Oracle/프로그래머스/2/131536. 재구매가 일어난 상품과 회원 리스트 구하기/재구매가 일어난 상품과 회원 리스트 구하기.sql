-- 코드를 입력하세요
SELECT USER_ID, PRODUCT_ID
FROM ONLINE_SALE
GROUP BY USER_ID, PRODUCT_ID
HAVING COUNT(PRODUCT_ID) >= 2
ORDER BY USER_ID ASC , PRODUCT_ID DESC

-- GROUP BY로 USER_ID와 PRODUCT_ID 두 컬럼을 함께 묶기
-- 그룹별 행 개수를 세서 2 이상인 그룹만 남기기 — 집계 결과에 조건을 걸 때는 WHERE가 아니라 어떤 절을 쓰는지 떠올려보세요 (H로 시작)
-- ORDER BY에서 USER_ID는 오름차순(기본값), PRODUCT_ID는 DESC