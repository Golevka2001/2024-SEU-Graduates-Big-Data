-- 毕业生总人数
SELECT COUNT(DISTINCT seu_card_id) FROM gbd_graduate_personal_stat;

-- 借阅量最大值
SELECT MAX(total_borrowed_books_num) FROM gbd_library_borrowing_stat;