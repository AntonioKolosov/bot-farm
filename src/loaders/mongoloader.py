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
        """Load all avaible files"""
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

    def load_content(self, type: str, ref: str) -> dict | str:
        """Load content from right database"""
        collection = self.__get_db_collection("Content")
        cursor: Cursor = collection.find({"name": ref})  # type: ignore
        content = ''
        for document in cursor:
            content = document
        return content

    def load_state(self, type: str, ref: str) -> str:
        """Load state"""
        collection = self.__get_db_collection("States")
        cursor: Cursor = collection.find({"state_id": ref})  # type: ignore
        state = ''
        for document in cursor:
            state = str(document["state_value"]).lower()
        return state

    def save_state(self, type: str, ref: str, state: str):
        """Save state"""
        collection = self.__get_db_collection("States")
        state_obj = {
            "state_id": ref,
            "state_value": state
        }
        collection.insert_one(state_obj)  # type: ignore

    def load_webview(self, app: str, ref: str, page: str) -> str:
        """Load webview from right database"""
        collection = self.__get_db_collection(app.lower().capitalize())
        cursor: Cursor = collection.find({})  # type: ignore
        views = ''
        webview = ''
        for document in cursor:
            views = document[ref]
            webview = \
                next(x for x in views if x['name'] == page)['webview']
        return webview

    def load_style(self, app: str, ref: str, style: str) -> str:
        """Load webstyle from right database"""
        collection = self.__get_db_collection(app.lower().capitalize())
        cursor: Cursor = collection.find({})  # type: ignore
        styles = ''
        webstyle = ''
        for document in cursor:
            styles = document[ref]
            webstyle = \
                next(x for x in styles if x['name'] == style)['webstyle']
        return webstyle

    def load_script(self, app: str, ref: str, script: str) -> str:
        """Load webscript from right database"""
        collection = self.__get_db_collection(app.lower().capitalize())
        cursor: Cursor = collection.find({})  # type: ignore
        scripts = ''
        webscript = ''
        for document in cursor:
            scripts = document[ref]
            webscript = \
                next(x for x in scripts if x['name'] == script)['script']
        return webscript
