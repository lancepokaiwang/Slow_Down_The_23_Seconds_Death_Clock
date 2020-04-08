import pymongo

client = pymongo.MongoClient("localhost", 27017)
db = client["University"]
collection = db["Dept2"]

dept = {
    "Name": "Computer",
    "Chair": {
        "Name": "Scott",
        "Hobbies": ["Reading", "Walking"]
    },
    "Professors": [
        {
            "Name": "James",
            "Hobbies": ["Skiing", "Walking"],
            "Students": [
                {
                    "Name": "Adams",
                    "Hobbies": ["Skiing", "Soccer"]
                },
                {
                    "Name": "David",
                    "Hobbies": ["Hiking"]
                },
                {
                    "Name": "Lewis",
                    "Hobbies": ["Travel", "Walking"]
                }
            ]
        },
        {
            "Name": "Henry",
            "Hobbies": ["Boating", "Fishing"],
            "Students": [
                {
                    "Name": "Maria",
                    "Hobbies": ["Dancing"]
                },
                {
                    "Name": "Kevin",
                    "Hobbies": ["Skating", "Reading"]
                },
                {
                    "Name": "Robin",
                    "Hobbies": []
                }
            ]
        }
    ]
}

dept = [
    {
        "_id": "Adams", "Hobbies": ["Skiing", "Soccer"]
    },
    {
        "_id": "David", "Hobbies": ["Hiking"]
    },
    {
        "_id": "Lewis", "Hobbies": ["Travel", "Walking"]
    },
    {
        "_id": "Maria", "Hobbies": ["Dancing"]
    },
    {
        "_id": "Kevin", "Hobbies": ["Skating", "Reading"]
    },
    {
        "_id": "Robin", "Hobbies": []
    },
    {
        "_id": "James", "Hobbies": ["Skiing", "Walking"], "Students":["Adams", "David", "Lewis"]
    },
    {
        "_id": "Henry", "Hobbies": ["Boating", "Fishing"], "Students":["Maria", "Kevin", "Robin"]
    },
    {
        "_id": "Scott", "Hobbies": ["Reading", "Walking"]
    },
    {
        "_id": "Computer", "Chair": "Scott", "Professors":["James", "Henry"]
    }
]

collection.insert_many(dept)

# result = collection.find({}, {"Professors.Students.Hobbies":1 , "_id":0})

# result = collection.aggregate( [{ "hobbies": { "$mergeObjects": "$Professors.Students.Hobbies" } }])
#
# for r in result:
#     print(r)


"""

db.getCollection('Dept2').aggregate([
    {
        $lookup: {
            from: "Dept2",
            localField: "Chair",    // field in the orders collection
            foreignField: "_id",  // field in the items collection
            as: "Chair"
        }
    },
   {
      $replaceRoot: { newRoot: { $mergeObjects: [ { $arrayElemAt: [ "$Chair", 0 ] }, "$$ROOT" ] } }
   },
   {
        $lookup: {
            from: "Dept2",
            localField: "Professors",    // field in the orders collection
            foreignField: "_id",  // field in the items collection
            as: "Professors"
        }
    },
   {
      $replaceRoot: { newRoot: { $mergeObjects: [ { $arrayElemAt: [ "$Professors", 0 ] }, "$$ROOT" ] } }
   },
   {
        $lookup: {
            from: "Dept2",
            localField: "Professors.Students",    // field in the orders collection
            foreignField: "_id",  // field in the items collection
            as: "Professors.Students"
        }
    },
   {
      $replaceRoot: { newRoot: { $mergeObjects: [ { $arrayElemAt: [ "$Professors.Students", 0 ] }, "$$ROOT" ] } }
   }
])
"""
