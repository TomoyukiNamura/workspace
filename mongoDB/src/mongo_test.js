// データベース一覧
show dbs;

//データベース削除
//use test;
//db.dropDatabase();

// データベース作成、切替
use test;

// データベースの状態確認
db.stats();

//コレクション一覧
show collections;

// コレクション削除
db.user.drop();

// userコレクション(テーブル)にデータをインサート
db.user.insert({name:'mr.a', age:10, gender:'m', hobbies:['programming']});
db.user.insert({name:'mr.b', age:20, gender:'m', hobbies:['vi']});
db.user.insert({name:'ms.c', age:30, gender:'f', hobbies:['programming', 'vi']});
db.user.insert({name:'ms.d', age:40, gender:'f', hobbies:['cooking']});

// userコレクションのドキュメント(レコード)取得(_idはオートインクリメントされている)
db.user.find()

// userコレクションからnameフィールド(カラム)がms.cという値のドキュメントを検索
db.user.find( {name:'ms.c'} )

// userコレクションからageフィールド(カラム)が20以上のドキュメントを検索
db.user.find({
    age:{$gte:20}
})

// userコレクションからageフィールド(カラム)が20以上、かつgenderがmのドキュメントを検索
db.user.find(
    {age:{$gte:20}, gender:'m'}
)

db.user.find({
    $and:[
        {age:{$gte:20}}, 
        {gender:'m'}
    ]
})

// userコレクションからageフィールド(カラム)が20以上、かつgenderがmのドキュメントを検索
db.user.find({
    $or:[
        {age:{$gte:20}}, 
        {gender:'m'}
    ]
})

// userコレクションからnameとageのみ検索(_idは非表示)
db.user.find(
    {}, 
    {_id:0, name:1, age:1}
)

// nameフィールドがmr.aの一番初めのドキュメントに対し、のgenderフィールドをXに変換
db.user.update(
    {name:'mr.a'}, 
    {$set:{gender:'X'}}
)


// userコレクションのデータを全消去
db.user.remove({})




// jsonファイル読み込み(GUI操作、CUIの場合以下でいけるらしいが、動作未確認)
//mongoimport --db db_name --collection collection_name --type json --file hoge.json 

// データベースの状態確認
db.stats()

// コレクションのドキュメント(レコード)取得(_idはオートインクリメントされている)
db.test_json.find({})
db.test_json.find({}).count()


db.test_json.find({
    $and:[
        {'properties.BLOCK_NUM':{$ne:'0026T'}}, 
        {'properties.BLOCK_NUM':{$ne:'0027'}}, 
    ]
}).count()


