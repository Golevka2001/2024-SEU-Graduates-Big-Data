-- 填充表中为 null 或为空字符串的字段
-- same_birthdate_num : '0'
-- same_origin_num : '0'
-- network_online_days : '0'
-- network_flow : '0.00'
-- consumption_amount : '0.00'
-- consumption_times : '0'
-- highest_single_consumption_amount : '0.00'
-- course_selected_num : '0'
-- credits_obtained : '0.00'
-- papers_num : '0'
-- lecture_attended_times : '0'
-- srtp_project_num : '0'
-- srtp_score : '0.00'
-- volunteer_activity_num : '0'
-- volunteer_duration : '0.00'
-- practice_project_num : '0'
-- total_borrowed_books_num : '0'
-- longest_book_borrowing_days : '0 days 00:00:00'
-- gym_ordered_times : '0'
-- morning_exercise_times : '0'
UPDATE graduates_big_data.gbd_graduate_personal_stat
SET same_birthdate_num                = IF(same_birthdate_num IS NULL OR same_birthdate_num = '', '0',
                                           same_birthdate_num),
    same_origin_num                   = IF(same_origin_num IS NULL OR same_origin_num = '', '0', same_origin_num),
    network_online_days               = IF(network_online_days IS NULL OR network_online_days = '', '0',
                                           network_online_days),
    network_flow                      = IF(network_flow IS NULL OR network_flow = '', '0.00', network_flow),
    consumption_amount                = IF(consumption_amount IS NULL OR consumption_amount = '', '0.00',
                                           consumption_amount),
    consumption_times                 = IF(consumption_times IS NULL OR consumption_times = '', '0',
                                           consumption_times),
    highest_single_consumption_amount = IF(
            highest_single_consumption_amount IS NULL OR highest_single_consumption_amount = '',
            '0.00', highest_single_consumption_amount),
    course_selected_num               = IF(course_selected_num IS NULL OR course_selected_num = '', '0',
                                           course_selected_num),
    credits_obtained                  = IF(credits_obtained IS NULL OR credits_obtained = '', '0.00',
                                           credits_obtained),
    papers_num                        = IF(papers_num IS NULL OR papers_num = '', '0', papers_num),
    lecture_attended_times            = IF(lecture_attended_times IS NULL OR lecture_attended_times = '', '0',
                                           lecture_attended_times),
    srtp_project_num                  = IF(srtp_project_num IS NULL OR srtp_project_num = '', '0', srtp_project_num),
    srtp_score                        = IF(srtp_score IS NULL OR srtp_score = '', '0.00', srtp_score),
    volunteer_activity_num            = IF(volunteer_activity_num IS NULL OR volunteer_activity_num = '', '0',
                                           volunteer_activity_num),
    volunteer_duration                = IF(volunteer_duration IS NULL OR volunteer_duration = '', '0.00',
                                           volunteer_duration),
    practice_project_num              = IF(practice_project_num IS NULL OR practice_project_num = '', '0',
                                           practice_project_num),
    total_borrowed_books_num          = IF(total_borrowed_books_num IS NULL OR total_borrowed_books_num = '', '0',
                                           total_borrowed_books_num),
    longest_book_borrowing_days       = IF(longest_book_borrowing_days IS NULL OR longest_book_borrowing_days = '',
                                           '0 days 00:00:00', longest_book_borrowing_days),
    gym_ordered_times                 = IF(gym_ordered_times IS NULL OR gym_ordered_times = '', '0',
                                           gym_ordered_times),
    morning_exercise_times            = IF(morning_exercise_times IS NULL OR morning_exercise_times = '', '0',
                                           morning_exercise_times)
WHERE TRUE;
