from pymongo import MongoClient

class MongoManager:
    def __init__(self, connection_string):
        self.client = MongoClient(connection_string)
        self._is_connected = False

    def connect(self):
        self._is_connected = True

    def disconnect(self):
        self.client.close()
        self._is_connected = False

    def is_connected(self):
        return self._is_connected

    def get_database(self, database_name):
        if not self._is_connected:
            raise RuntimeError("MongoDB connection is not established.")
        return self.client[database_name]
