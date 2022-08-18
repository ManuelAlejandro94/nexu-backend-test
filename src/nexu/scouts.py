from datetime import datetime
from src.nexu.web import services


class Scouts(object):
    def __init__(
            self,
            database,
            collection
    ):
        self.database = database

        self.control = self.database.get_collection(collection)

    def search_brands(self, request):
        pipelines = [{"$group": {"_id": "$brand_name", "average_price":{"$avg": "$average_price"}}}]
        averages = self.control.aggregate(pipelines)
        return averages

    def find_by_brand(self, brand):
        results = self.control.find({"brand_name": brand})
        return results

    def insert_brand(self, brand):
        self.control.insert_one({
            "name": None,
            "average_price": 0,
            "brand_name": brand
        })

    def find_by_model_brand(self, brand, model):
        if model is None:
            model = {"$type": 10}
        results = self.control.find_one({"brand_name": brand, "name": model})
        return results

    def insert_model(self, request):
        self.control.insert_one(request)

    def update_model_empty(self, request):
        query = {"_id": request["_id"]}
        query_update = {"$set": {"name": request["name"], "average_price": request["average_price"]}}
        self.control.update_one(query, query_update)

    def find_by_model(self, model):
        results = self.control.find_one({"name": model})
        return results

    def update_model(self, request):
        query = {"_id": request["_id"]}
        query_update = {"$set": {"average_price": request["average_price"]}}
        self.control.update_one(query, query_update)

    def find_all_models(self):
        results = self.control.find({})
        return results

    def find_models_gl(self, greather, lower):
        results = self.control.find({"average_price": {"$gte": int(greather), "$lte": int(lower)}})
        return results

    def find_models_g(self, greather):
        results = self.control.find({"average_price": {"$gte": int(greather)}})
        return results

    def find_models_l(self, lower):
        results = self.control.find({"average_price": {"$lte": int(lower)}})
        return results
