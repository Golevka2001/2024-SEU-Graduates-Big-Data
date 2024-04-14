-- graduate_personal_stat/same_canteen_percentage
-- 计算最常去相同食堂的人数百分比

CREATE TEMPORARY TABLE temp_table AS
SELECT most_frequent_consumption_place, COUNT(*) as temp_same_canteen_count
FROM graduate_personal_stat
GROUP BY most_frequent_consumption_place;

UPDATE graduate_personal_stat
SET same_canteen_num = (SELECT temp_same_canteen_count
                       FROM temp_table
                       WHERE temp_table.most_frequent_consumption_place = graduate_personal_stat.most_frequent_consumption_place);