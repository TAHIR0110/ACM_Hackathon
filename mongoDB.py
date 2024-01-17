#While instaling mongodb make sure to tick "Install mongodb as a Service" AND "Install mongodb compass" 
#install mongodb windows: https://www.mongodb.com/try/download/community
#install mongodb macos : https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-os-x/
#install mongodb shell: https://www.mongodb.com/try/download/shell OR download MongoDB for VS Code Extension on VSC
#Set a new env PATH variable for mongosh.exe
#pip install pymongo
import pymongo

try:
    client = pymongo.MongoClient("mongodb+srv://Anand:<>@cluster0.nljrcso.mongodb.net/?retryWrites=true&w=majority")
except:
    print("Error"+ Exception)


mymongoDB = client["ACM_Hackathon"]
collection = mymongoDB["User Info"]


#collection.insert_one()
#collection.delete_one()
#collection.update_one()

records = collection.find({})
for i in records:
    print(i)
