# -*- coding: utf-8 -*-

import sys
sys.path.append("/Users/tomoyuki/paper_bot/src/lib")

import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
from db import Mongo

SECONDS  = 20

TITLE_RM_LIST = ["Title:"]
AUTHERS_RM_LIST = ["Authors:"]
SUBMIT_DATE_RM_LIST = ["\n  \n  \n  \n    \n  \n  \n    \n    \n  \n\n  ", "(", ")", "Submitted on "] 
ABST_RM_LIST = ["Abstract:  ", "\n"]

HOST       = 'localhost'
PORT       = 27017
DB         = 'paper_bot'
COLLECTION = 'paper'


def str_clean(string, rm_list):
    for tmp_str in rm_list: string = string.replace(tmp_str, "")
    return string

def html_read(html):
    try:
        bsobj = BeautifulSoup(html.read())
        return bsobj
    except:
        print("error")

def get_paper_contents(bsobj, pdf_url):
    # タイトルの文字列を取得
    title = bsobj.findAll("h1",{"class":"title mathjax"})[0].text
    title = str_clean(title, TITLE_RM_LIST)
    
    # 著者の文字列を取得
    authors = bsobj.findAll("div",{"class":"authors"})[0].text
    authors = str_clean(authors, AUTHERS_RM_LIST)
    
    # 投稿日の文字列を取得
    submit_date = bsobj.findAll("div",{"class":"dateline"})[0].text
    submit_date = str_clean(submit_date, SUBMIT_DATE_RM_LIST)
    
    # アブストの文字列を取得
    abstract = bsobj.findAll("blockquote",{"class":"abstract mathjax"})[0].text
    abstract = str_clean(abstract, ABST_RM_LIST)
    
    # ドキュメント初期化
    document = {}
    
    # ドキュメントへ格納
    document["title"]       = title
    document["pdf_url"]     = pdf_url
    document["auther"]      = authors
    document["submit_date"] = submit_date
    document["abstract"]    = abstract
    
    # 出力
    return document


def main():
    # DBに入れる場合DBに接続
    mongo = Mongo(HOST, PORT, DB, COLLECTION)
    
    # アブストとpdfのURL取得
    abs_url = f"https://arxiv.org/abs/1912.11464"
    pdf_url = f"https://arxiv.org/pdf/1912.11464"
    
    # スクレイピング実行(指定時間ストップ)
    bsobj = html_read(urlopen(abs_url))
    time.sleep(SECONDS)
    
    # 論文内容を取得
    document = get_paper_contents(bsobj, pdf_url)
    
    # ドキュメントをmongoDBへ保存
    mongo.insert(document)
    
    # find
    docs = mongo.find(filters={})
    for doc in docs:
        print(doc)
