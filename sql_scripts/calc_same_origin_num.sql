-- graduate_personal_stat/same_origin_num
-- 计算生源地相同的毕业生人数

CREATE TEMPORARY TABLE temp_table AS
SELECT origin, COUNT(*) as temp_same_origin_count
FROM graduate_personal_stat
GROUP BY origin;

UPDATE graduate_personal_stat
SET same_origin_num = (SELECT temp_same_origin_count
                       FROM temp_table
                       WHERE temp_table.origin = graduate_personal_stat.origin);