#While instaling mongodb make sure to tick "Install mongodb as a Service" AND "Install mongodb compass" 
#install mongodb windows: https://www.mongodb.com/try/download/community
#install mongodb macos : https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-os-x/
#install mongodb shell: https://www.mongodb.com/try/download/shell OR download MongoDB for VS Code Extension on VSC
#Set a new env PATH variable for mongosh.exe
#pip install pymongo
import pymongo

try:
    client = pymongo.MongoClient("mongodb+srv://Anand:Prestonplayz-1@cluster0.nljrcso.mongodb.net/?retryWrites=true&w=majority")
except:
    print("Error"+ Exception)


mymongoDB = client["ACM_Hackathon"]
collection = mymongoDB["User Info"]


#collection.insert_one({"name":"atharv","age":20})
#collection.delete_one()
#collection.delete_one()
#collection.update_one()
user_data = collection.find_one({}, { "sort": { "createdAt": -1 } })
for i in user_data:
    print(i)

