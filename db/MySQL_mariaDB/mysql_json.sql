# データベースコマンド
show databases;            # データベース一覧
-- create database test;      # データベース作成
-- drop database test;        # データベース削除
use tmp;                  # データベース切り替え
select database();         # 接続中のデータベース表示
select version();          # データベースサーバのバージョン確認

# テーブル一覧
show tables;

# テーブル作成
CREATE TABLE features (
 id INT NOT NULL AUTO_INCREMENT,
 feature JSON NOT NULL,
 PRIMARY KEY (id),
 CHECK (JSON_VALID(feature))      # 無効な JSON データに対する制約
);
-- drop table features;

# カラム一覧
show columns from features;

# jsonファイル読み込み
LOAD DATA local infile '/Users/tomoyuki/python_workspace/SegNet_tensorflow/test_data/json/features.json' INTO TABLE features (feature);

## データ情報
###  データセレクト
select * from features limit 3;

## レコード数
SELECT COUNT(*) FROM features;

## 条件検索
### 下記構造のjsonを想定
-- { 
-- 	"type": "Feature", 
-- 	"properties": { 
-- 		"MAPBLKLOT": "0001001", 
-- 		"BLKLOT": "0001001", 
-- 		"BLOCK_NUM": "0001", 
-- 		"LOT_NUM": "001", 
-- 		"FROM_ST": "0", 
-- 		"TO_ST": "0", 
-- 		"STREET": "UNKNOWN", 
-- 		"ST_TYPE": null, 
-- 		"ODD_EVEN": "E" 
-- 	}, 
-- 	"geometry": { 
-- 		"type": "Polygon", 
-- 		"coordinates": [ 
-- 			[ 
-- 				[ -122.422003528252475, 37.808480096967251, 0.0 ], 
-- 				[ -122.422076013325281, 37.808835019815085, 0.0 ], 
-- 				[ -122.421102174348633, 37.808803534992904, 0.0 ], 
-- 				[ -122.421062569067274, 37.808601056818148, 0.0 ], 
-- 				[ -122.422003528252475, 37.808480096967251, 0.0 ] 
-- 			] 
-- 		] 
-- 	} 
-- }
SELECT * FROM features WHERE JSON_CONTAINS(feature, '"O"', '$.properties.ODD_EVEN') ;
SELECT COUNT(*) FROM features WHERE JSON_CONTAINS(feature, '"O"', '$.properties.ODD_EVEN') ;

select * from features limit 3;

select COUNT(*) from features where JSON_CONTAINS(feature, '"E"', '$.properties.ODD_EVEN');

# 静的ピボット
## テーブル初期化
CREATE TABLE json_data (
 id INT NOT NULL AUTO_INCREMENT,
 d_type varchar(20) NOT NULL,
 blklot varchar(20) NOT NULL,
 odd_even varchar(20) NOT NULL,
 STREET varchar(20) NOT NULL,
 PRIMARY KEY (id)
);

-- drop table json_data;
show columns from json_data;

## インサート
insert into json_data (d_type, blklot, odd_even, STREET) 
select 
	json_extract(feature, '$.type'),
	json_extract(feature, '$.properties.BLKLOT'),
	json_extract(feature, '$.properties.ODD_EVEN'),
	json_extract(feature, '$.properties.STREET')
from features;

select * from json_data;
select count(*) from json_data;

# ユニーク要素取得
select distinct concat(odd_even) from json_data order by odd_even;
select distinct concat(STREET) from json_data order by STREET;

# null補完
update json_data set odd_even='"NULL"' where odd_even is null or odd_even='' or odd_even='null';
update json_data set STREET='"NULL"' where STREET is null or STREET='' or STREET='null';


-- select 
-- 	id,
-- 	json_extract(feature, '$.type') as type,
-- 	json_extract(feature, '$.properties.BLKLOT') as BLKLOT,
-- 	json_extract(feature, '$.properties.ODD_EVEN') as ODD_EVEN
-- from features
-- WHERE JSON_CONTAINS(feature, '"O"', '$.properties.ODD_EVEN')
-- limit 3;


# 動的ピボット(参考：https://codeday.me/jp/qa/20190511/798101.html)
show columns from json_data;
select * from json_data;

SET @sql = NULL;
SELECT GROUP_CONCAT(DISTINCT CONCAT('min(case when STREET = ''',STREET,''' then id end) AS ', STREET)) INTO @sql FROM json_data;
SET @record = 'd_type';
SET @table_name = 'json_data';
SET @sql = CONCAT('SELECT ', @record,', ', @sql, ' FROM ' , @table_name,' GROUP BY ', @record);
select @sql;

PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;


# CONCAT、DISTINCT、GROUP_CONCAT
select CONCAT('max(case when odd_even = ''', odd_even,''' then id end) AS ', odd_even) FROM json_data;
select DISTINCT CONCAT('max(case when odd_even = ''', odd_even,''' then id end) AS ', odd_even) FROM json_data;
select GROUP_CONCAT(DISTINCT CONCAT('max(case when odd_even = ''', odd_even,''' then id end) AS ', odd_even)) FROM json_data;


# 度数分布表
show columns from json_data;
SET @tmp = 'STREET';
PREPARE s2 FROM CONCAT('SELECT count(id) as count, ', @tmp,' FROM json_data GROUP BY ', @tmp);
EXECUTE s2;





select id,json_extract(feature, '$.properties') as properties from features limit 3;
select id,json_extract(feature, '$.properties.BLKLOT') as BLKLOT from features limit 3;
select id,json_extract(feature, '$.properties.BLOCK_NUM') as BLOCK_NUM from features limit 3;

select max(case when json_extract(feature, '$.properties.ODD_EVEN')='E' then id end) as aaa from features;
select min(case when json_extract(feature, '$.properties.ODD_EVEN')='E' then id end) as aaa from features;

# 条件検索
## ODD_EVENがEの場合のidを検索
select (case when json_extract(feature, '$.properties.ODD_EVEN')='E' then id end) as aaa from features;

## BLKLOTが0001001の場合のLOT_NUMを検索
select max(case when json_extract(feature, '$.properties.BLKLOT')='0001001' then json_extract(feature, '$.properties.LOT_NUM') end) as aaa from features;

## ODD_EVENでグループ化した時のODD_EVEN、idの最小値、最大値
select json_extract(feature, '$.properties.ODD_EVEN') as ODD_EVEN, min(id), max(id) from features group by json_extract(feature, '$.properties.ODD_EVEN');

select GROUP_CONCAT(DISTINCT concat('max(case when', , 'then', id, 'end)')) from features;

select GROUP_CONCAT(DISTINCT CONCAT(
      'max(case when part_type = ''',
      json_extract(feature, '$.properties.ODD_EVEN'),
      ''' then part_id end) AS ',
      json_extract(feature, '$.properties.ODD_EVEN')
    )) INTO @sql from features;
   
select @sql

# 動的ピボットテーブル(カラム数不定)
SET @sql = NULL;
SELECT
  GROUP_CONCAT(DISTINCT
    CONCAT(
      'max(case when json_extract(feature, '$.properties.ODD_EVEN') = ''',
      part_type,
      ''' then json_extract(feature, '$.properties.BLKLOT') end)',
      as json_extract(feature, '$.properties.ODD_EVEN')
    )
  ) INTO @sql
FROM
  feature;
SET @sql = CONCAT('SELECT product_id, ', @sql, ' 
                  FROM parts 
                   GROUP BY product_id');

PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;




# ストアドルーチン
select SPECIFIC_NAME,ROUTINE_TYPE from information_schema.ROUTINES;

## ストアドプロシージャ(戻り値がない)
show procedure status;
show procedure status where Db='test';

CREATE PROCEDURE sample01()
	SELECT NOW();

call sample01();

CREATE PROCEDURE sample02( IN x INT )
	SELECT x + 1;

call sample02(3);



## ストアドファンクション(戻り値がある)
show function status;
show function status where Db='test';


-- select table_name, table_rows from information_schema.TABLES where table_schema = 'test';
-- select ROUTINE_NAME, ROUTINE_TYPE from information_schema.ROUTINES;


# ユーザー定義変数
SET @number = 3;
select @number;
SHOW USER_VARIABLES

SHOW VARIABLES where Variable_name LIKE 'number';

# 変数
SHOW VARIABLES where Variable_name LIKE 'character%';
SET group_concat_max_len = 65535;
SHOW VARIABLES where Variable_name LIKE 'group_concat_max_len';

