# データベースコマンド
show databases;            # データベース一覧
-- create database test;      # データベース作成
-- drop database test;        # データベース削除
use test;                  # データベース切り替え
select database();         # 接続中のデータベース表示


# テーブルコマンド
## テーブル一覧
show tables;

## テーブル作成 
CREATE TABLE goods(
	商品 VARCHAR(100) NOT NULL,
	価格 INTEGER NOT NULL,
	PRIMARY KEY (商品)
) ENGINE=INNODB;

CREATE TABLE purchase(
	店舗名 VARCHAR(100) NOT NULL,
	購入者名 VARCHAR(100) NOT NULL,
	商品 VARCHAR(100) NOT NULL,
	購入数 INTEGER NOT NULL,
	PRIMARY KEY (店舗名,購入者名,商品),
    FOREIGN KEY (商品)
      REFERENCES goods (商品)
      ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=INNODB;
show columns from purchase;

-- CREATE TABLE parent (
--     id INT NOT NULL,
--     PRIMARY KEY (id)
-- ) ENGINE=INNODB;
-- 
-- CREATE TABLE child (
--     id INT, 
--     parent_id INT,
--     INDEX par_ind (parent_id),
--     FOREIGN KEY (parent_id) 
--         REFERENCES parent(id)
--         ON DELETE CASCADE
-- ) ENGINE=INNODB;


-- drop table child;
-- drop table parent;
drop table purchase;
drop table goods;
drop table features;

## 外部キー追加
ALTER TABLE purchase
    ADD FOREIGN KEY 商品 REFERENCES goods (商品)



## テーブル削除
-- drop table goods;
-- drop table purchase;


# データ閲覧
## カラム情報確認
show columns from goods;
show columns from purchase;



## 全データ
select * from goods;
select * from purchase;


# データロード
## csv
load data local infile '/Users/tomoyuki/Desktop/purchase_2.csv' into table goods fields
terminated by ','                      # 区切り文字
ENCLOSED BY '"'                        # 文字列？
-- lines terminated by '\r\n'             # 改行コード
ignore 1 lines                         # ヘッダがある場合の指定
(商品, 価格); 

load data local infile '/Users/tomoyuki/Desktop/purchase_1.csv' into table purchase fields
terminated by ','                      # 区切り文字
ENCLOSED BY '"'                        # 文字列？
-- lines terminated by '\r\n'             # 改行コード
ignore 1 lines                         # ヘッダがある場合の指定
(店舗名, 購入者名, 商品, 購入数); 



# 文字コード
show variables like "chara%";   # 設定確認

