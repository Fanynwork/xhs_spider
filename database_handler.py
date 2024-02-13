import pymongo


def init_database():
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client['graduateDesign']['xhs_旅行']

    return db


def save_to_database(db, data_dic, url):
    try:
        db.insert_one(data_dic)
    except:
        print("")
        print("数据保存失败，错误url:", url)
