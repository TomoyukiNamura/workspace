# -*- coding: utf-8 -*-

import sys
sys.path.append("/Users/tomoyuki/paper_bot/src/lib")

import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
from db import Dynamo
from boto3.dynamodb.conditions import Key, Attr

SECONDS  = 20

TITLE_RM_LIST = ["Title:"]
AUTHERS_RM_LIST = ["Authors:"]
SUBMIT_DATE_RM_LIST = ["\n  \n  \n  \n    \n  \n  \n    \n    \n  \n\n  ", "(", ")", "Submitted on "] 
ABST_RM_LIST = ["Abstract:  ", "\n"]

REGION_NAME            = "ap-northeast-1."
ENDPOINT_URL           = "http://localhost:8000"
AWS_ACCESS_KEY_ID      = "ACCESS_ID"
AWS_SECRET_ACCESS_KEY  = "ACCESS_KEY"

TABLE_NAME = "paper_contents"
KEY_SCHEMA = [
    {
        'AttributeName': 'series',
        'KeyType': 'HASH'
    },
    {
        'AttributeName': 'title',
        'KeyType': 'RANGE'
    },
]
ATTRIBUTE_DEFINITIONS  = [
    {
        'AttributeName': 'series',
        'AttributeType': 'S'
    },
    {
        'AttributeName': 'title',
        'AttributeType': 'S'
    }
]
PROVISIONED_THROUGHPUT = {
    'ReadCapacityUnits': 1,
    'WriteCapacityUnits': 1
}


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
    document["series"]      = "mahine_learning"
    document["title"]       = title
    document["pdf_url"]     = pdf_url
    document["auther"]      = authors
    document["submit_date"] = submit_date
    document["abstract"]    = abstract
    
    # 出力
    return document


def main():
    # DBに接続
    dynamo = Dynamo(region_name=REGION_NAME, endpoint_url=ENDPOINT_URL, aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY, 
                    table_name=TABLE_NAME, key_schema=KEY_SCHEMA, attribute_definitions=ATTRIBUTE_DEFINITIONS, provisioned_throughput=PROVISIONED_THROUGHPUT)
    
    # アブストとpdfのURL取得
    abs_url = f"https://arxiv.org/abs/1912.11464"
    pdf_url = f"https://arxiv.org/pdf/1912.11464"
    
    # スクレイピング実行(指定時間ストップ)
    bsobj = html_read(urlopen(abs_url))
    time.sleep(SECONDS)
    
    # 論文内容を取得
    document = get_paper_contents(bsobj, pdf_url)
    
    # ドキュメントをmongoDBへ保存
    dynamo.put_items([document])

    # scan
    dynamo.scan(filter_expression=Attr("series").eq("mahine_learning"))
    
    len(dynamo.scan(filter_expression=Attr("title").eq(document["title"])))
    
    

#dynamo.delete_table("paper_contents")


