from pymongo import MongoClient

# Source DB (Infofarjax on farjaxapps)
source_uri = "YOUR_SOURCE_MONGODB_URI"
source_client = MongoClient(source_uri)
source_db = source_client["Infofarjax"]

# Target DB (fiot_prod_WebApps on New farjazit)
target_uri = "YOUR_TARGET_MONGODB_URI"
target_client = MongoClient(target_uri)
target_db = target_client["fiot_prod_WebApps"]

# Clone all collections
for collection_name in source_db.list_collection_names():
    source_collection = source_db[collection_name]
    target_collection = target_db[collection_name]

    print(f"Copying '{collection_name}'...")

    # Clear target collection first (optional)
    target_collection.delete_many({})

    # Fetch all documents and insert into target
    docs = list(source_collection.find())
    if docs:
        target_collection.insert_many(docs)

print("✅ Database migration completed.")
