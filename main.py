from pymongo import MongoClient

client_local = MongoClient('localhost', 27017)
local_db = client_local['my_local_database']
local_collection = local_db['my_collection']

username = "Artem"
password = "artemovich"
cluster_name = "Cluster0"
atlas_uri = f"mongodb+srv://Artem:artemovich@cluster0.6zltqqd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client_atlas = MongoClient(atlas_uri)
atlas_db = client_atlas['my_atlas_database']
atlas_collection = atlas_db['my_collection']

for document in local_collection.find():
    atlas_collection.insert_one(document)

client_local.close()
client_atlas.close()