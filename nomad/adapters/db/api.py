from pymongo import MongoClient

from nomad.utils import utils


class MongoAdapters(object):
    def __init__(self, host, port, db):
        self.client = MongoClient(host, int(port))
        self.db = self.client[db]

    def get_all_destinations(self, state, collection):
        collection = self.db[collection]
        output = []
        for destination in collection.find({"state": state}):
            output.append(
                {
                    "name": destination["name"],
                    "city": destination["city"],
                    "rating": destination["rating"],
                }
            )
        output = sorted(output, key=lambda k: k["rating"], reverse=True)
        return {"result": output}

    def add_destinations(
        self, name, city, pincode, state, tin, state_code, rating, collection
    ):
        collection = self.db[collection]
        count = collection.count_documents({"name": name, "pincode": pincode})
        if count == 0:
            collection_id = collection.insert(
                {
                    "name": name,
                    "city": city,
                    "pincode": pincode,
                    "creation_time": utils.get_current_time(),
                    "state": state,
                    "tin": str(tin),
                    "state_code": state_code,
                    "rating": rating,
                }
            )
            return {"result": str(collection_id)}
        else:
            return {"result": "Place already registered"}
