import json

class JSONUtil:
    @staticmethod
    def read_data(file_path):
        with open(file_path,"r") as file:
            data=json.load(file)
        return [(user["username"],user["password"]) for user in data["users"]]