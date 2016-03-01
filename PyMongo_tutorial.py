import pymongo
from pymongo import MongoClient

client = MongoClient()  # no arguments = localhost:27017

db = client.restaurants  # database
coll = db.restaurants_data  # collection


def printme(data):
    counter = 0
    for document in data:
        counter += 1
        print(document)  # prints the results one-by-one
    print("Returned results: ", counter)


# cursor = db.restaurants_data.find({"borough": "Manhattan", "cuisine": "Mexican"}, {"name": 1, "_id": 0})
# cursor = db.restaurants_data.find({"name": "Juni"}, {"name": 1, "cuisine": 1, "_id": 0})
# printme(cursor)

'''
result = db.restaurants_data.update_one(
        {"name": "Juni"},
        {"$set": {"cuisine": "American(New)"},
         "$currentDate": {"lastModified": True}}
)
'''
'''
result = db.restaurants_data.update_many(
        {"address.zipcode": "10016", "cuisine": "Other"},
        {
            "$set": {"cuisine": "Category to be determined"},
            "$currentDate": {"lastModified": True}
        }
)
'''

# result = db.restaurants_data.delete_many({"name": ""})
# print("Mathched: ", result.matched_count)
# print("Modified: ", result.modified_count)
# print("Deleted: ", result.deleted_count)

# cursor = db.restaurants_data.find({"cuisine": "Category to be determined"}, {"name": 1, "borough": 1, "_id": 0})
# printme(cursor)
# cursor = db.restaurants_data.find({"name": "Juni"}, {"name": 1, "cuisine": 1, "_id": 0})
# printme(cursor)

'''
cursor = db.restaurants_data.find({"$or": [{"cuisine": "Italian"}, {"cuisine": "Mexican"}]}, {"name": 1, "_id": 0}).sort(
    [
        ("borough", pymongo.DESCENDING),
        ("adress_zipcode", pymongo.ASCENDING)
    ]
)
'''
'''
cursor = db.restaurants_data.aggregate(
        [
            {"$group": {"_id": "$borough", "count": {"$sum": 1}}}
        ]
)  # group by borough name
printme(cursor)
'''
'''
cursor = db.restaurants_data.aggregate(
    [
        {"$match": {"borough": "Queens", "cuisine": "Brazilian"}},
        {"$group": {"_id": "$address.zipcode", "count": {"$sum": 1}}}
    ]
)
printme(cursor)
'''





