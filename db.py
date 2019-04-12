import pymongo
import time


# dblist = myclient.list_database_names()
# print(dblist)

name = "王大弟"
age = 13
gender = "m"
telephpne = "183728979238"

zhusu = "oYOaf1Mj_Y4PLS6OqwqdRKPoJ3xw"
xianbinshi = "oCsX1wgDmgVH2VDLbfklwRFKPZVI"
chubuzhenduan = "参宿四"


class DatabaseManager():
  
  def __init__(self, client_url="mongodb://root:Xdcrcqs123@dds-uf607532bf5fe7e41.mongodb.rds.aliyuncs.com:3717,dds-uf607532bf5fe7e42.mongodb.rds.aliyuncs.com:3717/admin?replicaSet=mgset-14016667", db_name="qianshan", collection_name="Binli"):
    self.clientAddress = pymongo.MongoClient(client_url)
    databaseName = clientAddress[db_name]
    collcetionTable = databaseName[collection_name]

  def createList(name="unknow",age=0,gender="x",telephpne=13000000000,zhusu=None,xianbinshi=None,chubuzhenduan=None):
    mylist = {
      "userinfo":{
        "name": name,
        "age": age,
        "gender": gender,
        "telephone": telephpne
      },
      "complaint": "",
      "ill": "",
      "diagnosis": "",
    }
    print(mylist)
    return mylist


if __name__ == '__main__':
  Db = DatabaseManager()
  mylist= Db.createList(name,age=age,gender=gender,telephpne=telephpne,zhusu=zhusu,xianbinshi=xianbinshi,chubuzhenduan=chubuzhenduan)
  x = mycol.insert_one(mylist)