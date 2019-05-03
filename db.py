import pymongo
import time
import sys
from bson.objectid import ObjectId

# reload(sys)
# sys.encoding('utf-8')
# dblist = myclient.list_database_names()
# print(dblist)


class DatabaseManager():
  
  def __init__(self, client_url="mongodb://root:puchi2019@db.stemaker.top:27003/?authSource=admin", db_name="qianshan", collection_name="Binli"):
    self.clientAddress = pymongo.MongoClient(client_url)
    self.databaseName = self.clientAddress[db_name]
    self.collcetionTable = self.databaseName[collection_name]
    print("collection succed")

  def createItem(self, name="unknow",age=0,gender="x",telephpne=13000000000,zhusu=None,ill=None,chubuzhenduan=None):
    mylist = {
      "userInfo":{
        "name": name,
        "age": age,
        "gender": gender,
        "telephone": telephpne
      },
      "complaint": zhusu,
      "ill": ill,
      "diagnosis": chubuzhenduan
    }
    x = self.collcetionTable.insert_one(mylist)
    return x.inserted_id

  def getAll(self):
    dict_db = []
    for x in self.collcetionTable.find().sort("_id", 1):
      print(x)
      x['_id'] = str(x['_id'])
      dict_db.append(x)
    return dict_db
      
  def updateItem(self, id, updateInfo):
    query = { '_id': ObjectId(id) }
    newValue = { "$set": updateInfo }
    x = self.collcetionTable.update_one(query, newValue)
    return x

  def deleteItem(self, id):
    # query = { '_id': ObjectId(id) }
    query = { '_id': ObjectId(id) }
    x = self.collcetionTable.delete_one(query)
    return x

  def deleteItems(self):
    # query = { '_id': ObjectId(id) }
    query = { 'userinfo': {'$exists': True }}
    x = self.collcetionTable.delete_many(query)
    return x

if __name__ == '__main__':
  name = "王大弟"
  age = 13
  gender = "m"
  telephpne = "183728979238"

  zhusu = "oYOaf1Mj_Y4PLS6OqwqdRKPoJ3xw"
  ill = "oCsX1wgDmgVH2VDLbfklwRFKPZVI"
  chubuzhenduan = 'djisn'

  mg = "mongodb://root:puchi2019@db.stemaker.top:27003/?authSource=admin"

  Db = DatabaseManager()
  mylist= Db.createItem(name="dfa", age=age, gender=gender,telephpne=telephpne,zhusu=zhusu,ill=ill,chubuzhenduan=chubuzhenduan)
  Db.deleteItems()
  print(mylist)