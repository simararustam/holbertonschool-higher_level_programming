-- Write a script that creates 
-- the MySQL server user user_0d_1
CREATE USER IF NOT EXIST 'user_0d_1'@'localhost';
GRANT ALL PRIVELEGES ON *.* for 'user_0d_1'@'localhost';
