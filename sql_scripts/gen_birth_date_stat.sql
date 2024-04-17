# 清除表中原有数据
TRUNCATE TABLE gbd_birth_date_stat;

# 插入数据，统计gbd_graduate_personal_stat表中birth_date的分布
INSERT INTO gbd_birth_date_stat (birth_date, count)
SELECT
    birth_date,
    COUNT(*) AS count
FROM
    gbd_graduate_personal_stat
GROUP BY
    birth_date;