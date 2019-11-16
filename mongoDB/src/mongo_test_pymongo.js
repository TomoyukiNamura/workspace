// データベース作成、切替
use test;

// データベースの状態確認
db.stats()

// testコレクション(テーブル)のドキュメント(レコード)取得(_idはオートインクリメントされている)
db.test.find()

db.test.find({
    $and:[
        {'properties.BLOCK_NUM':{$ne:'0026T'}}, 
        {'properties.BLOCK_NUM':{$ne:'0027'}}, 
    ]
}).count()

// typeとproperties.BLOCK_NUMのカラムのみ表示
db.test.find({}, {'type':1, 'properties.BLOCK_NUM':1})

// properties.BLOCK_NUMのユニークデータを取得
db.test.distinct('properties.BLOCK_NUM', {}).forEach(get_results)


function get_results (result) {
    print(tojson(result));
}


var wa = function (b){print(b);} 

var func = function (result) {
    print(tojson(result));
}
print(func)



db.test.distinct('properties.BLOCK_NUM', {}).forEach(wa)



aa = db.test.distinct('properties.BLOCK_NUM', {})
aa.forEach(wa)


var num = 1;

num = num * 2;

