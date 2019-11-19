-- データベースコマンド
select * from pg_database; -- データベース一覧
--create database test;      -- データベース作成
--drop database test;        -- データベース削除
select current_database(); -- 接続中のデータベース表示

-- テーブル一覧
select relname as table_name from pg_stat_user_tables;

-- テーブル作成
CREATE TABLE features (
	id SERIAL NOT NULL,
	feature JSON NOT NULL,
	PRIMARY KEY (id)
);

---- カラム一覧
select * from information_schema.columns
where table_catalog='test' and table_name='features'
order by ordinal_position;


-- jsonファイル読み込み
LOAD DATA local infile '/Users/tomoyuki/Desktop/features.json' INTO TABLE features (feature);


COPY features (feature) FROM '/Users/tomoyuki/Desktop/features3.json';

\copy features (feature) FROM '/Users/tomoyuki/Desktop/features3.json';


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



