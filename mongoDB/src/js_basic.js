// javascript基礎文法(参考：https://jsprimer.net/basic/)

// 変数と宣言
//// const: 再代入できない変数の宣言とその変数が参照する値（初期値）を定義
const bookTitle = "JavaScriptの本";
bookTitle = "aaa";

//// let: 値の再代入が可能な変数を宣言
let bookTitle2 = "JavaScriptの本";
bookTitle2 = "pythonの本";

//// var: 値の再代入が可能な変数を宣言(同じ名前の変数を再定義できてしまう、変数の巻き上げと呼ばれる意図しない挙動がある => letを使う方が良い)
var bookTitle3 = "JavaScriptの本";
var bookTitle3 = "pythonの本";


// データ型
//// 真偽値（Boolean）: trueまたはfalseのデータ型
let bool = true;
typeof bool;

//// 数値（Number）: 42 や 3.14159 などの数値のデータ型
let num = 3.14159265358979;
typeof num;

//// 文字列（String）: "JavaScript" などの文字列のデータ型
let str = "JavaScript";
typeof str;

//// undefined: 値が未定義であることを意味するデータ型
let undef;
typeof undef;

//// null: 値が存在しないことを意味するデータ型
let nl = null;
typeof nl;

//// シンボル（Symbol）: ES2015から追加された一意で不変な値のデータ型
typeof Symbol("シンボル");

//// 配列
let list = [1,2,3,4,5];
typeof list;

//// 辞書
let dict = { "key": "value" };
typeof dict;

//// 関数
let func = function (a, b) {print(a+b);};
typeof func;
func(4, 5);


// 条件分岐
let x = 42;
if (x > 10) {
    print("xは10より大きな値です");
} else if (x === 10) {
    print("xは10です");
} else {
    print("xは10より小さな値です");
}

// ループと反復処理
//// while文
let x = 0;
print(`ループ開始前のxの値: ${x}`);
while (x < 10) {
    print(x);
    x += 1;
}
print(`ループ終了後のxの値: ${x}`);

//// for文
let total = 0;
for (let i = 0; i < 10; i++) {
    total += i + 1;
}
print(total);

//// forEach
let array = [1, 2, 3];
array.forEach(currentValue => {
    print(currentValue);
});

