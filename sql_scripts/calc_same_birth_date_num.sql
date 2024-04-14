-- graduate_personal_stat/same_birth_date_num
-- 计算出生日期相同的毕业生人数

CREATE TEMPORARY TABLE temp_table AS
SELECT birth_date, COUNT(*) as temp_same_birth_date_count
FROM graduate_personal_stat
GROUP BY birth_date;

UPDATE graduate_personal_stat
SET same_birth_date_num = (SELECT temp_same_birth_date_count
                           FROM temp_table
                           WHERE temp_table.birth_date = graduate_personal_stat.birth_date);