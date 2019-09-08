import pymongo
client = pymongo.MongoClient('localhost',27017)
mydb = client['mydb']
test = mydb['test']
#此时连接到了数据库，并新建了数据库以及test数据集合，但只有插入数据后才能显示出数据库
test.insert_one({'name':'jan','sex':'男','grade':89})