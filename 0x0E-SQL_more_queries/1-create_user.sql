-- A script that creates my sql server
-- And also grants it all its privileges
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL ON *.* TO user_0d_1@localhost;
