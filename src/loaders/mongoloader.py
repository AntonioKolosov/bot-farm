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
        self.__df_storage = cfg.df_storage
        print("Storage", self.__storage)

    def load_names(self):
        """Load all avaible bot's names"""

        uri = self.__storage.split("-----")[0]

        print(uri)

        with MongoClient(uri) as client:
            db_name = self.__storage.split("-----")[1]
            db = client[db_name]
            collection = db['MetaData']
            cursor: Cursor = collection.find({})  # type: ignore
            names = []
            for document in cursor:  # type: ignore
                st = str(document["service_type"]).lower()
                sa = str(document["service_alias"]).lower()
                name = f'{st}___{sa}'
                names.append(name)
            return names

    def load_metadata(self, name: str) -> dict:
        """Load metadata from right database"""

        uri = self.__storage.split("-----")[0]

        print(uri)

        with MongoClient(uri) as client:
            db_name = self.__storage.split("-----")[1]
            db = client[db_name]
            collection = db['MetaData']
            st, sa = name.split('___')
            cursor: Cursor = collection.find({"service_type": st.upper(),
                                             "service_alias": sa.upper()})  # type: ignore # noqa: E501
            doc = list(cursor)
            return doc[0]  # type: ignore

    def load_content(self, name: str) -> dict | str:
        """Load content from right database"""

        uri = self.__df_storage.split("-----")[0]
        # uri='mongodb://0.tcp.ngrok.io:19741'
        print(uri)

        with MongoClient(uri) as client:
            db_name = self.__df_storage.split("-----")[1]
            db = client[db_name]
            collection = db['Content']
            cursor: Cursor = collection.find({"name": name})  # type: ignore
            doc = list(cursor)
            return doc[0]  # type: ignore
