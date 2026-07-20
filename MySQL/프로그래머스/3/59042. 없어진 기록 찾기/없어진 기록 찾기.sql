-- 입양을 간 기록은 있는데, 보호소에 들어온 기록이 없는 동물
SELECT ANIMAL_ID
      ,NAME
FROM ANIMAL_OUTS O 
-- 보호소에 들어간 기록이 없는 동물
WHERE NOT EXISTS (
    SELECT 1
    FROM ANIMAL_INS I 
    WHERE I.ANIMAL_ID = O.ANIMAL_ID 
)
ORDER BY ANIMAL_ID ASC