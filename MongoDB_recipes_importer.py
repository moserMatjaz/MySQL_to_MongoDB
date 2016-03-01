import MySQLdb
from pymongo import MongoClient

client = MongoClient()  # connnect to Mongo
db = client.recipes  # connnect to Mongo

db_MySQL = MySQLdb.connect("localhost", "root", "morphling", "summer_project_4")  # connect to MySQL
cursor = db_MySQL.cursor()  # connect to MySQL
cursor2 = db_MySQL.cursor()


def area_insert():
    cursor.execute("SELECT * from area")
    results = cursor.fetchall()
    counter = 0
    for row in results:
        counter += 0
        area_id, area_name = row
        result = db.areas.insert_one({
            "id": area_id,
            "name": str('"' + area_name + '"')
        })
        print(result.inserted_id)
    print(counter)


def cuisine_insert():
    cursor.execute("SELECT * from cuisine")
    results = cursor.fetchall()
    counter = 0
    for row in results:
        counter += 0
        cuisine_id, cuisine_name, cuisine_scope, cuisine_area = row
        result = db.cuisines.insert_one({
            "id": cuisine_id,
            "name": str('"' + cuisine_name + '"'),
            "scope": str('"' + cuisine_scope + '"'),
            "area": str('"' + cuisine_area + '"')
        })
        print(result.inserted_id)
    print(counter)


def ingredient_insert():
    cursor.execute("SELECT * from ingredient")
    results = cursor.fetchall()
    counter = 0
    for row in results:
        counter += 0
        ingredient_id, ingredient_name, ingredient_category = row
        result = db.ingredient.insert_one({
            "id": ingredient_id,
            "name": str('"' + ingredient_name + '"'),
            "category": str('"' + ingredient_category + '"')
        })
        print(result.inserted_id)
    print(counter)


def recipe_insert():
    cursor.execute("SELECT * from recipe ORDER BY id DESC")
    results = cursor.fetchall()
    counter = 0
    for row in results:
        counter += 0
        recipe_id, recipe_source, recipe_cuisine = row
        result = db.recipe.insert_one({
            "id": recipe_id,
            "source": str('"' + recipe_source + '"'),
            "cuisine": str('"' + recipe_cuisine + '"'),
            "ingredients": []
        })
        print(result.inserted_id)

    cursor2.execute("SELECT * from ingred_recipe ORDER BY id_rec DESC")
    results = cursor2.fetchall()
    for row in cursor2:
        ingredient, id_recipe = row
        result = db.recipe.update(
            {"id": id_recipe},
            {"$addToSet": {"ingredients": ingredient}}
        )
        print("Updated: ", id_recipe, " with ingredient: ", ingredient)
    # print(counter)


recipe_insert()
area_insert()
cuisine_insert()
ingredient_insert()