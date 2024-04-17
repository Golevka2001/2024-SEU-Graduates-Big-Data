# 清除表中原有数据
TRUNCATE TABLE gbd_origin_stat;

# 插入数据，统计gbd_graduate_personal_stat表中origin的分布
INSERT INTO gbd_origin_stat (origin, count)
SELECT
    origin,
    COUNT(*) AS count
FROM
    gbd_graduate_personal_stat
GROUP BY
    origin;