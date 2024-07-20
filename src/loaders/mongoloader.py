"""
Mongo loader - Loads a topic metadata and content from MongoDB
"""


from sqlite3 import Cursor
from pymongo.mongo_client import MongoClient

from .loader import Loader
from ..config import cfg


class MongoLoader(Loader):
    """Load metadata and content from MongoDB"""
    def __init__(self, type: str) -> None:
        super().__init__(type)
        self.__storage = cfg.storage
        print("Storage", self.__storage)
        self.__database = ""
        self.__connect()

    def __connect(self):
        """Create connection with Mongo and Atlas"""
        client = self.__client()
        self.__database = self.__create_database(client)

    def __client(self) -> MongoClient:
        """Create client to connect Cluster"""
        uri = self.__storage.split("-----")[0]
        print(uri)
        client = MongoClient(uri)
        try:
            client.admin.command("ping")
            print("Connected to MongoDB!")
        except Exception as e:
            raise Exception(f'__client error: {e}')
        return client

    def __create_database(self, client: MongoClient):
        """Create connection to Database"""
        try:
            client = self.__client()
            print(self.__storage.split("-----")[1])
            db = client[self.__storage.split("-----")[1]]
            return db
        except Exception as e:
            raise Exception(f'__database error: {e}')

    def __get_db_collection(self, col_name):
        """Get collection from database"""
        try:
            collection = self.__database[col_name]
        except Exception as e:
            raise Exception(f'__collection error: {e}')
        return collection

    def load_names(self):
        """Load all avaible bot's names"""
        collection = self.__get_db_collection("MetaData")
        cursor = collection.find({})  # type: ignore
        names = []
        for document in cursor:  # type: ignore
            st = str(document["service_type"]).lower()
            sa = str(document["service_alias"]).lower()
            name = f'{st}___{sa}'
            names.append(name)
        return names

    def load_metadata(self, name: str) -> dict:
        """Load metadata from right database"""
        st, sa = name.split('___')
        collection = self.__get_db_collection("MetaData")  # type: ignore
        cursor: Cursor = collection.find({"service_type": st.upper(),
                                          "service_alias": sa.upper()})  # type: ignore # noqa: E501
        doc = list(cursor)
        return doc[0]  # type: ignore

    def load_content(self, ref: str) -> dict | str:
        """Load content from right database"""
        collection = self.__get_db_collection("Content")
        cursor: Cursor = collection.find({"name": ref})  # type: ignore
        content = ''
        for document in cursor:
            content = document
        return content
