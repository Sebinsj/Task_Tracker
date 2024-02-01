from model import Todo

#mongodb driver
import motor.motor_asyncio

client=motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')

database=client.TodoList
collection=database.todo

async def fetch_one_todo(title):
    document=await collection.find_one({"title":title})
    retrun document