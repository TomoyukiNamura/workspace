import sqlite3
import itertools

#import configparser
#import json

#inifile = configparser.SafeConfigParser()
#inifile.read("./config.ini", encoding="utf-8")
#
#language = {"python":json.loads(inifile["TYPE"]["python"])}


DB_NAME = "EDICT_cleaned_r2.sqlite3"



# 対象カラムがnullでないレコードを，対象テーブルから取得
def _tmp_search(conn, table_name, item):
    search_result_list = []
    
    select_sql = f"select * from {table_name} where {item} is not null;" 
    cur = conn.cursor()
    for row in cur.execute(select_sql):
        search_result_list.append(row)
    cur.close()
    
    return search_result_list

# 入力した日本語と一致するレコードを，対象テーブルから取得
def _search_records_from_table(conn, input_data, table_name, item):
    search_result_list = []
    
    select_sql = f"select * from {table_name} where {item} like '{input_data}';" 
    cur = conn.cursor()
    for row in cur.execute(select_sql):
        search_result_list.append(row)
    cur.close()
    
    return search_result_list

# 入力した日本語と一致するレコードを再帰的に探索
def _recursive_search(conn, table_name, input_chr):
    # 漢字完全一致，漢字前方一致，漢字部分一致
    # ひらがな完全一致，ひらがな前方一致，ひらがな部分一致
    # カタカナ完全一致，カタカナ前方一致，カタカナ部分一致
    # の順で検索をかける
    item_list = ["jpn", "jpn_hira", "jpn_kata"]
    input_chr_list = [input_chr, f"{input_chr}%", f"%{input_chr}%"]
    
    for tmp_item in item_list:        
        for tmp_input_chr in input_chr_list:  
            
            search_result_list = _search_records_from_table(conn=conn, input_data=tmp_input_chr, table_name=table_name, item=tmp_item)
            #print(search_result_list)
            if len(search_result_list)>0:
                break
            
        if len(search_result_list)>0:
            break
    
    return search_result_list


# 探索したレコードをプリント
def _print_search_results(search_result_list):
    for search_result in search_result_list:
        print_txt = ""
        for i in range(len(search_result)):
            if search_result[i]==None:
                break
            print_txt = f"{print_txt}{search_result[i]} | "
        print(print_txt)


# 探索したレコードから英単語をリストで取得
def _get_eng(search_result_list):
    eng_list = []
    
    for search_result in search_result_list:
        for i in range(5,len(search_result)):
            if search_result[i]==None:
                break
            
            if search_result[i] not in eng_list:
                eng_list.append(search_result[i])
                
    return eng_list

# DBの各テーブル名を表示
def _check_tables(conn):
    select_sql = "select name from sqlite_master where type='table'"
    cur = conn.cursor()
    for row in cur.execute(select_sql):
        print_txt = ""
        for i in range(len(row)):
            print_txt = f"{print_txt}{row[i]}"
        print(print_txt)
    cur.close()

# 指定したテーブルの全レコードを表示
def _check_table_records(conn, table_name):
    select_sql = f"select * from {table_name}" 
    cur = conn.cursor()
    for row in cur.execute(select_sql):
        print_txt = ""
        for i in range(len(row)):
            if row[i]!=None:
                print_txt = f"{print_txt}{row[i]} | "
        
        print(print_txt)
    cur.close()    

# 指定したテーブルのカラム名を表示
def _check_table_columns(conn, table_name):
    select_sql = f"pragma table_info({table_name})" 
    cur = conn.cursor()
    for row in cur.execute(select_sql):
        print_txt = ""
        for i in range(len(row)):
            if row[i]!=None:
                print_txt = f"{print_txt}{row[i]} | "
        
        print(print_txt)
    cur.close()    

# 対象の英単語と一致するレコードから，指定した型を抽出
def _get_target_case(eng, case, conn, table_name, eng_item_name):
    result = None
    select_sql = f"select {case} from {table_name} where {eng_item_name} like '{eng}' limit 1" 
    cur = conn.cursor()
    for row in cur.execute(select_sql):
        result = row[0]
    cur.close()
    return result


def _make_product_list(list_1, list_2, case):
    result = []
    p = itertools.product(list_1, list_2)
    for v in p:
        if case == "constant":
            tmp = f"{v[0]}_{v[1]}"
        elif case == "pascal":
            tmp = f"{v[0]}{v[1]}"
        elif case == "camel":
            tmp = f"{v[0]}{v[1].title()}"
        elif case == "snake":
            tmp = f"{v[0]}_{v[1]}"
        elif case == "kebab":
            tmp = f"{v[0]}-{v[1]}"
        result.append(tmp)
    return result
        
        
# main
def shika(input_data):

#    ## DB内確認
#    with sqlite3.connect(f"dict/{DB_NAME}") as conn:
#        # DBの各テーブル名
#        _check_tables(conn)
#        
        # 指定したテーブルのカラム名，レコード
#        table_name = "name"
#        _check_table_columns(conn, table_name)
#        _check_table_records(conn, table_name)
        
#        # 対象の英単語と一致するレコードから，指定した型を抽出
#        eng = "to go about one's work"
#        tmp = _get_target_case(eng = eng, case=case, conn=conn, table_name="name", eng_item_name="eng")
#        print(tmp)


    # input_dataを展開
    input_sentence = input_data["sentence"]
    case = input_data["case"]
    case_associated_type = input_data["type"]
    #acronym = input_data["acronym"]
    
    # caseが指定なし=空欄の場合，case_associated_typeで置き換える
    if case == "":
        case = case_associated_type
        
    ## DBに接続
    with sqlite3.connect(f"dict/{DB_NAME}") as conn:
        # 英単語検索結果保存場所を初期化
        eng_cand_list = []
        
        # 各文字に対して，英単語検索を実施
        #input_sentence = ['混同', '行列', '三浦',"海岸"]
        for input_chr in input_sentence:
            #input_chr = "たち"
            
            # DBからレコードを検索
            search_result_list = _recursive_search(conn, "edict", input_chr)
            
            # 英単語のみを抽出
            eng_cand = _get_eng(search_result_list)
            
            # eng_listの各要素を指定の型に変更
            """
            シングルクォーテーションのついた英単語が検索できない問題あり
            """
            for i in range(len(eng_cand)):
                eng_cand[i] = _get_target_case(eng = eng_cand[i], case=case, conn=conn, table_name="name", eng_item_name="eng")
            
            # 保存
            eng_cand_list.append(eng_cand)
        
        
    # eng_cand_listの各リスト要素を連結
    convert_list = eng_cand_list[0]
    for i in range(1, len(eng_cand_list)):    
        convert_list = _make_product_list(convert_list, eng_cand_list[i], case)
      
        
    # convert_listの一番最初の要素を出力結果とする
    if len(convert_list) > 0:
        result = convert_list[0]
    else:
        result = "検索結果なし"

    return result, convert_list




        
        