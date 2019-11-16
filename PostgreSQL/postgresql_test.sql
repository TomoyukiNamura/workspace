-- データベースコマンド
select * from pg_database; -- データベース一覧
create database test;      -- データベース作成
drop database test;        -- データベース削除
use test;                  -- データベース切り替え
select current_database(); -- 接続中のデータベース表示

-- テーブルコマンド
---- テーブル一覧
select relname as TABLE_NAME from pg_stat_user_tables;

---- カラム一覧
select * from information_schema.columns 
where table_catalog='postgres' and table_name='test' 
order by ordinal_position;







-- テーブルコマンド
--CREATE TABLE staff
--(id    CHAR(4)    NOT NULL,
--name   TEXT       NOT NULL,
--age    INTEGER    ,
--PRIMARY KEY (id));


--CREATE TABLE hoge
--(id    CHAR(4)    NOT NULL,
--name   TEXT       NOT NULL,
--age    INTEGER    ,
--PRIMARY KEY (id));

--drop table staff;
--drop table hoge;
--drop table hugo;


CREATE TABLE test
(id    INTEGER    NOT NULL,
col1   INTEGER    NOT NULL,
col2   INTEGER    NOT NULL,
col3   INTEGER    NOT NULL,
PRIMARY KEY (id));

COPY test (id, col1, col2, col3) FROM '/home/test.csv' CSV HEADER;
\COPY test (id, col1, col2, col3) FROM '/Users/tomoyuki/Desktop/test.csv' CSV HEADER;




select * from test;



