-- Script to convert hbtn_0c_0 database, first_table table, and name field to UTF8
USE hbtn_0c_0;

-- Convert the database to utf8mb4
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert the first_table table to utf8mb4
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert the name field in the first_table table to utf8mb4
ALTER TABLE first_table MODIFY COLUMN name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
