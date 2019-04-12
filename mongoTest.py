import pymongo
import time

client_url="mongodb://root:Xdcrcqs123@dds-2ze4640ee59336841.mongodb.rds.aliyuncs.com:3717,dds-2ze4640ee59336842.mongodb.rds.aliyuncs.com:3717/admin?replicaSet=mgset-14019471"
clientAddress = pymongo.MongoClient(client_url)
databaseName = clientAddress['qianshan']
collcetionTable = databaseName['test']

collist = databaseName.list_collection_names()
print(collist)