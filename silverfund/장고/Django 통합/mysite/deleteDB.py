#기존 DB에 남아있는 파일(이전 분기에 수집한) 지우기
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["연금상품DB"]

for i in range(1,9):
    mycol = mydb[f"main_funds{i}"]
    mycol.delete_many({})