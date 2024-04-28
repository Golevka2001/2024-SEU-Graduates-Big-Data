# 清除表中原有数据
TRUNCATE TABLE gbd_favorite_canteen_stat;

# 插入数据，统计gbd_graduate_personal_stat表中most_frequent_consumption_place的分布
INSERT INTO gbd_favorite_canteen_stat (canteen_name, count)
SELECT most_frequent_consumption_place,
       COUNT(*) AS count
FROM gbd_graduate_personal_stat
GROUP BY most_frequent_consumption_place;