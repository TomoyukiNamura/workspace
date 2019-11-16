#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from pymongo import MongoClient


HOST       = '192.168.0.7'
PORT       = 27017
DB         = 'test'
COLLECTION = 'test'

class TestMongo(object):

    def __init__(self, host, port, db):
        self.clint = MongoClient(host=host, port=port)
        self.db = self.clint[db]
        
    def insert(self, collection, data):
        print('insert start...')
        self.db[collection].insert_many(data)
        print('done.')
    
    def drop_collection(self, collection):
        print('drop collection start...')
        self.db[collection].drop()
        print('done.')

def main():
    # mongoDBに接続、データベース初期化
    obj = TestMongo(HOST, PORT, DB)

    # 指定のコレクションを削除
    obj.drop_collection(COLLECTION)
    
    # jsonデータインポート
    with open('./data/features.json', 'r') as f:
        data = [json.loads(line) for line in f]
        
    # 指定のコレクションにデータをインサート
    obj.insert(COLLECTION, data)
    


if __name__ == '__main__':
    main()
    
    

