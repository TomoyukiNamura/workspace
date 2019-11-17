// データベース作成、切替
use test;

// データベースの状態確認
db.stats()

// testコレクション(テーブル)のドキュメント(レコード)取得(_idはオートインクリメントされている)
db.test.find()

// typeとproperties.BLOCK_NUMのカラムのみ表示
db.test.find({}, {'type':1, 'properties.BLOCK_NUM':1})

// properties.BLOCK_NUMのユニークデータを取得
get_results = function (result) {
    print(tojson(result));
};
unique_list = db.test.distinct('properties.BLOCK_NUM', {});
unique_list.forEach(get_results);

// ダミーデータ作成
new_unique_list = [];
unique_list.forEach(x => {
    new_unique_list.push(x + "_" + x.slice(0,4));
});
new_unique_list

// ダミーデータを分割してdictにまとめる
dict = {};
new_unique_list.forEach(x => {
    tmp = x.split("_")
    if  (typeof dict[tmp[1]]==="undefined") {dict[tmp[1]] = {};};
    dict[tmp[1]][tmp[0]] = db.test.find({'properties.BLOCK_NUM':tmp[0]}).count();
});
dict



//
get_results = function (result) {
    print(tojson(result));
};
unique_list = db.test.distinct('properties.BLOCK_NUM', {});
unique_list.forEach(get_results);

// 集計結果をtest2コレクションにインサート
unique_list.forEach(x => {
    tmp_dict = {"id":x.slice(0,4), "name":x, "count":db.test.find({'properties.BLOCK_NUM':x}).count()};
    db.test2.insert(tmp_dict);
});
db.test2.find()

