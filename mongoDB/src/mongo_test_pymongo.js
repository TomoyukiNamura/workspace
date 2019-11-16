// データベース作成、切替
use test2

// データベースの状態確認
db.stats()

// userコレクション(テーブル)のドキュメント(レコード)取得(_idはオートインクリメントされている)
db.test.find()

db.test2.find()

db.aaa.find()

// データベースs1使用 


use test;

show collections;

// s1データベースのs2コレクションのドキュメントを取得
db.test.find()

