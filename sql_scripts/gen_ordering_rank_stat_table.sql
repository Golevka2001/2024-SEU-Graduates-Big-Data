-- 清除表中原有数据
TRUNCATE TABLE gbd_ordering_rank_stat;

-- 插入数据，统计gbd_graduate_personal_stat表中每个gym_ordered_times对应的排名
INSERT INTO gbd_ordering_rank_stat (ordering_times, ordering_rank)
SELECT CAST(COALESCE(NULLIF(gym_ordered_times, ''), '0') AS SIGNED INTEGER),
       RANK() OVER (ORDER BY CAST(gym_ordered_times AS SIGNED INTEGER) DESC)
FROM gbd_graduate_personal_stat
WHERE gym_ordered_times IS NOT NULL
ON DUPLICATE KEY UPDATE ordering_times = VALUES(ordering_times), ordering_rank = VALUES(ordering_rank);