from model import Todo

#mongodb driver
import motor.motor_asyncio

client=motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:2701')