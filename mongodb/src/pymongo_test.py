#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pymongo import MongoClient
from datetime import datetime

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
    
    # 指定のコレクションにデータをインサート
    data = [{'_id':1, 'title': 'ハリネズミ1','content': 'ハリネズミ可愛い~','created_at': datetime.now()},
            {'_id':2, 'title': 'ハリネズミ2','content': 'ハリネズミ可愛い~かな?','created_at': datetime.now()},
            {'_id':3, 'title': 'ハリネズミ3','content': 'ハリネズミ可愛いくない!','created_at': datetime.now()}]
    obj.insert(COLLECTION, data)
    


if __name__ == '__main__':
    main()
    
    

