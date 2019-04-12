import pymongo
import time

client_url="mongodb://root:Xdcrcqs123@dds-uf607532bf5fe7e41.mongodb.rds.aliyuncs.com:3717,dds-uf607532bf5fe7e42.mongodb.rds.aliyuncs.com:3717/admin?replicaSet=mgset-14016667"
clientAddress = pymongo.MongoClient(client_url)
databaseName = clientAddress['qianshan']
collcetionTable = databaseName['test']

collist = databaseName.list_collection_names()
print(collist)