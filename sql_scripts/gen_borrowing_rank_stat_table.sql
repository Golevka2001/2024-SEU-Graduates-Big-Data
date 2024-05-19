USE graduates_big_data;

-- 清除表中原有数据
TRUNCATE TABLE gbd_borrowing_rank_stat;

-- 插入数据，统计gbd_graduate_personal_stat表中每个total_borrowed_books_num对应的排名
INSERT INTO gbd_borrowing_rank_stat (borrowing_num, borrowing_rank)
SELECT CAST(COALESCE(NULLIF(total_borrowed_books_num, ''), '0') AS SIGNED INTEGER),
       RANK() OVER (ORDER BY CAST(total_borrowed_books_num AS SIGNED INTEGER) DESC)
FROM gbd_graduate_personal_stat
WHERE TRUE
ON DUPLICATE KEY UPDATE borrowing_num = VALUES(borrowing_num), borrowing_rank = VALUES(borrowing_rank);