from pymongo import MongoClient

client = MongoClient("<your mongodb secret srv url >")

db = client.sample_training

grade_collection = db["grades"]

