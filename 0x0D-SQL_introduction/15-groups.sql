-- Lists the scores with same numberr
SELECT `score`, COUNT(`score`) as `number` FROM `second_table` GROUP BY `score` ORDER BY `score` DESC;
